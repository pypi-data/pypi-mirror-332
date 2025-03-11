use std::{net::SocketAddr, sync::Arc, time::Duration};

use clap::Parser;
use log::{error, info, trace};
use tokio::{
    io::{AsyncReadExt, AsyncWriteExt},
    net::{
        tcp::{OwnedReadHalf, OwnedWriteHalf},
        TcpSocket, TcpStream,
    },
    sync::{
        mpsc::{Receiver, Sender},
        Mutex,
    },
    task::JoinHandle,
    time::{self, sleep},
};

use crate::{
    architecture::JlrArchitecture,
    args::SnapshotArgs,
    did::create_did_list,
    doip::{
        header::{
            payload::{
                diagnostic_message::DiagnosticMessage,
                diagnostic_message_nack::DiagnosticMessageNack,
                payload::{DoipPayload, PayloadType},
                routing_activation_request::RoutingActivationRequest,
                routing_activation_response::RoutingActivationResponse,
            },
            version::DoipVersion,
        },
        message::{
            activation_code::ActivationCode, activation_type::ActivationType,
            diagnostic_nack::DiagnosticNackNode, message::DoipMessage, node_type::NodeType,
        },
    },
    ecu::{Ecu, SnapshotEcu},
    error::{DoipDiscovery, DoipDiscoveryError, DoipSnapshotError, SnapshotError},
    output::{DIDOutput, DTCOutput, ECUOutput, Response},
    utils::{bytes_to_ascii, bytes_to_hex_string, get_custom_input},
};

#[derive(Debug)]
pub struct Snapshot {
    entity: NodeType,
    address: SocketAddr,
    logical_address: [u8; 2],
    pub ecus: Vec<Ecu>,
    pub snapshot_ecus: Vec<SnapshotEcu>,
    unknown_target_address: Arc<Mutex<Vec<[u8; 2]>>>,
    pub output: Arc<Mutex<Vec<ECUOutput>>>,
}

impl Snapshot {
    pub async fn new(
        entity: NodeType,
        address: &SocketAddr,
        logical_address: [u8; 2],
        arch: JlrArchitecture,
    ) -> Self {
        trace!(
            "Snapshot New (Init): {:?} | {:?} | {:?} | {:?}",
            &entity,
            &address,
            &logical_address,
            &arch
        );

        let mut s = Self {
            entity,
            address: *address,
            logical_address,
            ecus: arch.generate_ecus(),
            snapshot_ecus: Vec::<SnapshotEcu>::new(),
            unknown_target_address: Arc::new(Mutex::new(Vec::<[u8; 2]>::new())),
            output: Arc::new(Mutex::new(Vec::new())),
        };

        s.snapshot_ecus = s.init_snapshot_ecus().await;

        let mut output = s.prefill_output().await;
        s.output.lock().await.append(&mut output);

        trace!("Snapshot New (Return): {:?}", &s);
        s
    }

    async fn init_snapshot_ecus(&self) -> Vec<SnapshotEcu> {
        trace!("Init Snapshot ECUs (Init)");
        let mut ecus = match self.entity {
            NodeType::DoipGateway => self.ecus.clone(),
            NodeType::DoipNode => {
                let mut e = self.ecus.clone();
                e.retain(|ecu| ecu.address == self.logical_address);
                e
            }
        };

        let custom_ecus = match get_custom_input().await {
            Ok(ecus) => Some(ecus),
            Err(_) => None,
        };

        match custom_ecus {
            Some(mut ecus) => {
                match self.entity {
                    NodeType::DoipGateway => {}
                    NodeType::DoipNode => {
                        ecus.retain(|ecu| ecu.address == self.logical_address);
                    }
                };

                trace!("Init Snapshot ECUs (Return): {:?}", &ecus);
                ecus
            }
            None => {
                let dids = create_did_list();
                let new_ecus: Vec<SnapshotEcu> = ecus
                    .iter_mut()
                    .map(|ecu| SnapshotEcu {
                        name: ecu.name.clone(),
                        acronym: ecu.acronym.clone(),
                        address: ecu.address,
                        architecture: ecu.architecture.clone(),
                        dids: dids.clone(),
                    })
                    .collect();

                trace!("Init Snapshot ECUs (Return): {:?}", &ecus);
                new_ecus
            }
        }
    }

    async fn prefill_output(&self) -> Vec<ECUOutput> {
        trace!("Prefill Output (Init)");
        let mut output: Vec<ECUOutput> = vec![];

        for ecu in self.snapshot_ecus.iter() {
            let ecu_write = ECUOutput {
                name: ecu.name.to_string(),
                acronym: ecu.acronym.to_string(),
                address: bytes_to_hex_string(&ecu.address),
                dids: self.get_ecu_dids(ecu),
                dtcs: Vec::<DTCOutput>::new(),
            };
            output.push(ecu_write);
        }

        trace!("Prefill Output (Return): {:?}", &output);
        output
    }

    fn get_ecu_dids(&self, ecu: &SnapshotEcu) -> Vec<DIDOutput> {
        trace!("Get ECU DIDs (Init): {:?}", &ecu);
        let mut ret = Vec::<DIDOutput>::new();

        for did in ecu.dids.clone() {
            ret.push(DIDOutput {
                did: bytes_to_hex_string(&did.did).to_lowercase(),
                name: did.name.to_string(),
                response: Response {
                    ascii: String::new(),
                    hex: String::new(),
                },
            })
        }

        trace!("Get ECU DIDs (Return): {:?}", &ret);
        ret
    }

    pub async fn get_output(&self) -> Vec<ECUOutput> {
        trace!("Get Output (Init)");
        let output_lock = self.output.lock().await;

        trace!("Get Output (Return): {:?}", &output_lock);
        output_lock.clone()
    }
}

impl DoipSnapshot for Snapshot {
    async fn connect(&self) -> Result<TcpStream, DoipSnapshotError> {
        let sock = match TcpSocket::new_v4() {
            Ok(sock) => sock,
            Err(e) => {
                error!("Setup TCP Stream (Create Socket): {:?}", e);
                return Err(DoipSnapshotError::Io(e));
            }
        };

        let mut stream = match sock.connect(self.address).await {
            Ok(stream) => stream,
            Err(e) => {
                error!("Setup TCP Stream (Socket Connect): {:?}", e);
                return Err(DoipSnapshotError::Io(e));
            }
        };

        stream.set_nodelay(true).unwrap();

        let _ = self.get_routing_authentication(&mut stream).await;

        Ok(stream)
    }

    async fn snapshot(
        &self,
        stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<Vec<ECUOutput>, DoipSnapshotError> {
        trace!("Snapshot Snapshot (Init): {:?}", &stream);
        let (read_half, write_half) = match self.setup_tcp_stream(stream).await {
            Ok(stream) => stream,
            Err(e) => return Err(e),
        };

        let write_half_clone = write_half.clone();
        let read_half_clone = read_half.clone();

        let (logger_tx, logger_rx) = tokio::sync::mpsc::channel::<DoipMessage>(65536);
        let (parser_tx, parser_rx) = tokio::sync::mpsc::channel::<Vec<u8>>(65536);
        let (tcp_tx, tcp_rx) = tokio::sync::mpsc::channel::<DoipMessage>(65536);

        let _logger_handle = self.logger(logger_rx).await;
        let _parser_handle = self.parser(parser_rx, logger_tx).await;
        let mut reader_handle = self.tcp_reader(read_half, parser_tx).await;
        let mut writer_handle = self.tcp_writer(write_half, tcp_rx).await;

        let mut max_dids = 0;

        self.snapshot_ecus.iter().for_each(|ecu| {
            let did_len = ecu.dids.len();
            if did_len > max_dids {
                max_dids = did_len
            }
        });

        let delay = SnapshotArgs::parse().delay;

        for count in 0..max_dids {
            for ecu in self.snapshot_ecus.iter() {
                let did = match ecu.dids.get(count) {
                    Some(did) => did,
                    None => continue,
                };

                let unknown_target_address_lock = self.unknown_target_address.lock().await;
                if unknown_target_address_lock.contains(&ecu.address) {
                    sleep(Duration::from_millis(delay.into())).await;

                    continue;
                };

                drop(unknown_target_address_lock);

                let payload = DiagnosticMessage {
                    source_address: [0x0e, 0x80],
                    target_address: ecu.address,
                    message: [0x22, did.did[0], did.did[1]].to_vec(),
                };

                let msg = DoipMessage::new(DoipVersion::Iso13400_2012, Box::new(payload));

                let _ = tcp_tx.send(msg).await;

                // How can I get rid of this?
                sleep(Duration::from_millis(delay.into())).await;
            }
        }

        tokio::select! {
          _ = &mut reader_handle => {
            trace!("Reader task completed, aborting writer");
            writer_handle.abort();
        }
        _ = &mut writer_handle => {
            trace!("Writer task completed, aborting reader");
            reader_handle.abort();
        }
        };

        trace!("Snapshot Snapshot (Return)");

        let output = self.get_output().await;

        trace!(
            "Write Half Strong Count: {:?} - {}",
            Arc::strong_count(&write_half_clone),
            self.entity
        );
        trace!(
            "Read Half Strong Count: {:?} - {}",
            Arc::strong_count(&read_half_clone),
            self.entity
        );

        match self.entity {
            NodeType::DoipGateway => {}
            NodeType::DoipNode => {
                match (
                    Arc::into_inner(write_half_clone),
                    Arc::into_inner(read_half_clone),
                ) {
                    (Some(write_mtx), Some(read_mtx)) => {
                        let write_half_new = write_mtx.into_inner();
                        let read_half_new = read_mtx.into_inner();

                        let new_stream = write_half_new.reunite(read_half_new).unwrap();
                        new_stream.set_linger(Some(Duration::ZERO)).unwrap();
                        drop(new_stream);
                    }
                    _ => {
                        error!("Failed to drop node: {:?}", self.logical_address)
                    }
                };
            }
        };

        Ok(output)
    }

    async fn logger(&self, mut rx: Receiver<DoipMessage>) -> JoinHandle<()> {
        trace!("Logger (Init): {:?}", &rx);
        let unknown_target_address_clone = Arc::clone(&self.unknown_target_address);
        let output_clone = Arc::clone(&self.output);

        let handle = tokio::task::spawn(async move {
            info!("Logger Initialised");
            let mut output = output_clone.lock().await;

            while let Some(msg) = rx.recv().await {
                trace!("Logger Received: {:?}", &msg);
                let mut unknown_target_address_clone = unknown_target_address_clone.lock().await;

                match msg.header.payload_type {
                    PayloadType::DiagnosticMessage => {
                        match DiagnosticMessage::from_bytes(&msg.payload.to_bytes()) {
                            Some(doip_msg) => log_diagnostic_message(doip_msg, &mut output).await,
                            None => {}
                        };
                    }
                    PayloadType::DiagnosticMessageAck => (),
                    PayloadType::DiagnosticMessageNack => {
                        if let Some(msg) =
                            DiagnosticMessageNack::from_bytes(&msg.payload.to_bytes())
                        {
                            match msg.nack_code {
                                DiagnosticNackNode::UnknownTargetAddress => {
                                    unknown_target_address_clone.push(msg.source_address);
                                }
                                DiagnosticNackNode::OutOfMemory => (),
                                DiagnosticNackNode::TransportProtocolError => {}
                                _ => {}
                            };
                        }
                    }
                    _ => (),
                };
            }
        });

        trace!("Logger (Return): {:?}", &handle);
        handle
    }

    async fn tcp_writer(
        &self,
        write_half: Arc<Mutex<OwnedWriteHalf>>,
        mut rx: Receiver<DoipMessage>,
    ) -> JoinHandle<()> {
        trace!("TCP Writer (Init): {:?} | {:?}", &write_half, &rx);
        let handle = tokio::task::spawn(async move {
            info!("TCP Writer Initialised");

            while let Some(did) = rx.recv().await {
                let mut write = write_half.lock().await;
                let bytes = did.to_bytes();

                if let Err(e) = { write.write(&bytes).await } {
                    error!("TCP Writer (Message Write Error): {:?}", e);
                } else {
                    trace!("TCP Writer (Message Write): {:?}", bytes);
                }
            }
        });

        trace!("TCP Writer (Return): {:?}", &handle);
        handle
    }

    async fn tcp_reader(
        &self,
        read_half: Arc<Mutex<OwnedReadHalf>>,
        parser_tx: Sender<Vec<u8>>,
    ) -> JoinHandle<()> {
        trace!("TCP Reader (Init): {:?} | {:?}", &read_half, &parser_tx);
        let handle = tokio::task::spawn(async move {
            info!("TCP Reader Initialised");
            let mut buffer = [0; 65536];

            // Perform the first read without a timeout
            {
                // Acquiring the lock
                let mut read = read_half.lock().await;
                if let Ok(bytes) = read.read(&mut buffer).await {
                    let res = &buffer[..bytes].to_vec();
                    trace!("TCP Reader (Received): {:?}", res);

                    if let Err(e) = parser_tx.send(res.to_vec()).await {
                        error!("Failed to send parsed data: {:?}", e);
                        return;
                    }
                }
            }

            // Loop for subsequent reads with timeout
            loop {
                let mut read = read_half.lock().await;
                let timeout_duration = Duration::from_millis(2000);

                // Perform a read with a timeout
                let read_result = { time::timeout(timeout_duration, read.read(&mut buffer)).await };

                match read_result {
                    Ok(Ok(bytes)) => {
                        let res = &buffer[..bytes].to_vec();
                        trace!("TCP Reader (Received): {:?}", res);

                        if let Err(e) = parser_tx.send(res.to_vec()).await {
                            error!("Failed to send parsed data: {:?}", e);
                            break;
                        }
                    }
                    Ok(Err(e)) => {
                        error!("TCP Reader (Read Error): {:?}", e);
                        break;
                    }
                    Err(e) => {
                        error!("TIMEOUT: {}", e);
                        // Timeout branch
                        trace!("TCP Reader: 500ms timeout hit, returning.");
                        return;
                    }
                }
            }
        });
        trace!("TCP Reader (Return): {:?}", &handle);
        handle
    }

    async fn parser(
        &self,
        mut parser_rx: Receiver<Vec<u8>>,
        logger_tx: Sender<DoipMessage>,
    ) -> JoinHandle<()> {
        trace!("Parser (Init): {:?} | {:?}", &parser_rx, &logger_tx);
        let handle = tokio::task::spawn(async move {
            info!("Parser");

            while let Some(res) = parser_rx.recv().await {
                trace!("Parser Received: {:?}", &res);
                let msgs = match DoipMessage::parse_from_bytes(res.to_vec()) {
                    Ok(msgs) => msgs,
                    Err(e) => {
                        error!("TCP Reader (Message Parse): {:?}", e);
                        continue; // Stop processing if parsing fails.
                    }
                };

                for msg in msgs {
                    trace!("Parse (Read): {:?}", msg);
                    match logger_tx.send(msg).await {
                        Ok(log) => log,
                        Err(e) => {
                            error!("TCP Reader (Message Log): {:?}", e);
                            continue;
                        }
                    };
                }
            }
        });
        trace!("Parser (Return): {:?}", &handle);
        handle
    }

    async fn setup_tcp_stream(
        &self,
        stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>), DoipSnapshotError> {
        trace!("Setup TCP Stream (Init): {:?}", &stream);
        if let Some(stream) = stream {
            // If a stream is already provided, return it directly
            Ok(stream)
        } else {
            // Establish a new connection and split it
            let tcp_stream = self.connect().await.map_err(|_| {
                DoipSnapshotError::Snapshot(SnapshotError::DiscoveryError(
                    DoipDiscoveryError::DoipDiscovery(DoipDiscovery::NoNetworkFound),
                ))
            })?;

            let (read_half, write_half) = tcp_stream.into_split();
            Ok((
                Arc::new(Mutex::new(read_half)),
                Arc::new(Mutex::new(write_half)),
            ))
        }
    }

    async fn get_routing_authentication(
        &self,
        stream: &mut TcpStream,
    ) -> Result<RoutingActivationResponse, DoipSnapshotError> {
        trace!("Get Routing Authentication (Init): {:?}", &stream);
        let ra_req_payload = RoutingActivationRequest {
            source_address: [0x0e, 0x80],
            activation_type: ActivationType::Default,
            buffer: [0, 0, 0, 0],
        };

        let ra_req = DoipMessage::new(
            crate::doip::header::version::DoipVersion::Iso13400_2012,
            Box::new(ra_req_payload),
        );

        let _ = stream.write(&ra_req.to_bytes()).await;

        let mut buffer = [0; 65536];
        let bytes = match stream.read(&mut buffer).await {
            Ok(bytes) => bytes,
            Err(e) => {
                error!("Get Routing Authentication (Stream Read): {:?}", e);
                return Err(DoipSnapshotError::Io(e));
            }
        };

        let res = &buffer[..bytes];
        let msgs = match DoipMessage::parse_from_bytes(res.to_vec()) {
            Ok(msgs) => msgs,
            Err(e) => {
                error!("Get Routing Authentication (Message Parse): {:?}", e);
                return Err(DoipSnapshotError::Snapshot(SnapshotError::ParsingError(e)));
            }
        };

        for msg in msgs {
            match RoutingActivationResponse::from_bytes(&msg.payload.to_bytes()) {
                Some(ra_res) => match ra_res.activation_code {
                    ActivationCode::SuccessfullyActivated => {
                        trace!("Get Routing Authentication (Return): {:?}", &ra_res);
                        return Ok(ra_res);
                    }
                    code => {
                        error!(
                            "Get Routing Authentication (Activation Code Check Failed): {:?}",
                            code
                        );
                        return Err(DoipSnapshotError::Snapshot(
                            SnapshotError::FailedAuthenticationCheck,
                        ));
                    }
                },
                None => {
                    error!("Get Routing Authentication (Routing Activation Response Parse Failed)");
                    continue;
                }
            };
        }

        Err(DoipSnapshotError::Snapshot(
            SnapshotError::FailedToGetAuthentication,
        ))
    }
}

pub trait DoipSnapshot {
    async fn snapshot(
        &self,
        stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<Vec<ECUOutput>, DoipSnapshotError>;
    async fn logger(&self, rx: Receiver<DoipMessage>) -> JoinHandle<()>;
    async fn tcp_writer(
        &self,
        write_stream: Arc<Mutex<OwnedWriteHalf>>,
        rx: Receiver<DoipMessage>,
    ) -> JoinHandle<()>;
    async fn tcp_reader(
        &self,
        read_stream: Arc<Mutex<OwnedReadHalf>>,
        parser_tx: Sender<Vec<u8>>,
    ) -> JoinHandle<()>;
    async fn setup_tcp_stream(
        &self,
        stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>), DoipSnapshotError>;
    async fn get_routing_authentication(
        &self,
        stream: &mut TcpStream,
    ) -> Result<RoutingActivationResponse, DoipSnapshotError>;
    async fn parser(
        &self,
        parser_rx: Receiver<Vec<u8>>,
        logger_tx: Sender<DoipMessage>,
    ) -> JoinHandle<()>;
    async fn connect(&self) -> Result<TcpStream, DoipSnapshotError>;
}

async fn log_diagnostic_message(msg: DiagnosticMessage, output: &mut [ECUOutput]) {
    trace!("Logging Diagnostic Message (Init): {:?}", &msg);
    let payload = &msg.message;
    let _reply_flag = payload[0];
    let did = &payload[1..3];
    let message = &payload[3..];
    let message_ascii = match bytes_to_ascii(message) {
        Ok(msg) => msg,
        Err(_) => return,
    };

    for ecu in output.iter_mut() {
        if ecu.address == bytes_to_hex_string(&msg.source_address) {
            for ecu_did in ecu.dids.iter_mut() {
                if ecu_did.did.to_lowercase() == bytes_to_hex_string(did).to_lowercase() {
                    ecu_did.response = Response {
                        ascii: message_ascii.clone(),
                        hex: bytes_to_hex_string(message),
                    };
                    break;
                }
            }
            break;
        }
    }
    trace!("Logging Diagnostic Message (Return): {:?}", &msg);
}
