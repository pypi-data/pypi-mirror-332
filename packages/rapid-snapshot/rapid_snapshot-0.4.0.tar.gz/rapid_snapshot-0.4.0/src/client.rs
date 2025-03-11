use std::collections::HashSet;
use std::{
    collections::HashMap,
    net::{IpAddr, Ipv4Addr, SocketAddr},
    path::Path,
    sync::Arc,
    time::Duration,
};

use futures::future::join_all;
use log::{error, info, trace};
use network_interface::{Addr, NetworkInterface, NetworkInterfaceConfig};
use tokio::{
    fs::{self, File},
    io::{self, AsyncReadExt, AsyncWriteExt},
    net::{TcpSocket, TcpStream, UdpSocket},
    sync::Mutex,
    time::{self, sleep, Instant},
};

use crate::{
    doip::{
        header::{
            payload::{
                entity_status_request::EntityStatusRequest,
                entity_status_response::EntityStatusResponse,
                payload::{DoipPayload, PayloadType},
                routing_activation_request::RoutingActivationRequest,
                routing_activation_response::RoutingActivationResponse,
                vehicle_announcement_message::VehicleAnnouncementMessage,
                vehicle_identification_request::VehicleIdentificationRequest,
            },
            version::DoipVersion,
        },
        message::{
            activation_code::ActivationCode, activation_type::ActivationType, message::DoipMessage,
            node_type::NodeType,
        },
    },
    entity::DoipEntity,
    error::{
        DoipDiscovery, DoipDiscoveryError, DoipSnapshotError, ParseError, SnapshotError,
        TestForDoipError,
    },
    gateway::DoipGateway,
    host::Host,
    node::DoipNode,
    output::{ECUOutput, OutFileBase},
    utils::bytes_to_ascii,
    vehicle::Vehicle,
};

#[derive(Clone, Debug)]
pub struct Client {
    nodes: Vec<DoipNode>,
    gateway: DoipGateway,
    vehicle: Vehicle,
    host: Host,
}

impl Client {
    pub fn new() -> Self {
        trace!("New Client (Init)");
        Client::default()
    }

    pub async fn connect(&mut self) -> Result<TcpStream, DoipDiscoveryError> {
        trace!("Connect (Init)");
        let stream = self.discover_doip_networks().await;

        trace!("Connect (Return): {:?}", &stream);
        stream
    }

    pub async fn snapshot(&mut self) -> Result<(), DoipSnapshotError> {
        let now = Instant::now();
        trace!("Snapshot (Init)");
        let stream: TcpStream = match self.connect().await {
            Ok(stream) => stream,
            Err(e) => {
                return Err(DoipSnapshotError::Snapshot(SnapshotError::DiscoveryError(
                    e,
                )))
            }
        };

        let (read_half, write_half) = stream.into_split();

        // Wrap halves in Arc<Mutex<_>>
        let read_half = Arc::new(Mutex::new(read_half));
        let write_half = Arc::new(Mutex::new(write_half));

        let read_half_clone = Arc::clone(&read_half);
        let write_half_clone = Arc::clone(&write_half);

        let futures = self
            .nodes
            .iter_mut()
            .map(|node| node.snapshot(self.vehicle.architecture, None))
            .collect::<Vec<_>>();

        let (gateway_result, node_results) = tokio::join!(
            self.gateway
                .snapshot(self.vehicle.architecture, Some((read_half, write_half))),
            async { join_all(futures).await }
        );

        let mut outputs: Vec<ECUOutput> = gateway_result.unwrap_or_default();

        trace!("Gateway Output: {:?}", &outputs);

        trace!("Node Results: {:?}", &node_results);

        // Flatten and collect node_results into a HashMap for efficient lookups
        let node_outputs: HashMap<String, ECUOutput> = node_results
            .into_iter()
            .filter_map(|result| result.ok()) // Keep only the Ok variants
            .flatten() // Flatten Vec<Vec<ECUOutput>> into Vec<ECUOutput>
            .map(|ecu| (ecu.address.clone(), ecu)) // Map by address
            .collect();

        trace!("Node Outputs: {:?}", &node_outputs);

        // Update outputs with node_outputs
        for output in &mut outputs {
            trace!("Gateway Output (Output): {:?}", &output);
            if let Some(node_ecu) = node_outputs.get(&output.address) {
                trace!("Gateway Output (OutputIF): {:?}", &node_ecu);
                *output = node_ecu.clone(); // Replace output with corresponding node_ecu
            }
        }

        let elapsed = now.elapsed();

        match self.write_out(outputs, elapsed).await {
            Ok(_) => trace!("Write Out Successful"),
            Err(_) => error!("Write Out Failed"),
        };
        trace!("Snapshot (Return)");

        let write_mutex = Arc::into_inner(write_half_clone).unwrap();
        let write_half_new = write_mutex.into_inner();
        let read_mutex = Arc::into_inner(read_half_clone).unwrap();
        let read_half_new = read_mutex.into_inner();

        let new_stream = write_half_new.reunite(read_half_new).unwrap();
        new_stream.set_linger(Some(Duration::ZERO)).unwrap();
        drop(new_stream);

        Ok(())
    }

    async fn write_out(&self, ecus: Vec<ECUOutput>, time: Duration) -> io::Result<()> {
        trace!("Write Out (Init): {:?}", &ecus);
        match Path::new("C:\\PST").exists() {
            true => {}
            false => fs::create_dir("C:\\PST").await.unwrap(),
        };

        let vin = match bytes_to_ascii(&self.vehicle.vin) {
            Ok(vin) => vin,
            Err(_) => "VIN".to_string(),
        };

        let mut out_file = File::create(format!(
            "C:\\PST\\{:}_{}_{:}.json",
            self.host.hostname,
            vin,
            self.host.exec_start.as_millis(),
        ))
        .await
        .unwrap();

        let output: OutFileBase = OutFileBase {
            vin,
            distance: 0,
            voltage: 0,
            interior_temperature: 0,
            exterior_temperature: 0,
            power_mode: 0,
            ecus,
            version: format!("v{}", env!("CARGO_PKG_VERSION")),
            time_taken: time.as_nanos(),
        };

        let serialized = serde_json::to_string_pretty(&output).unwrap();
        trace!("Serialised: {:?}", &serialized);
        out_file.write_all(serialized.as_bytes()).await
    }

    async fn discover_doip_networks(&mut self) -> Result<TcpStream, DoipDiscoveryError> {
        trace!("Discover Doip Networks (Init)");
        let ips = self.filter_network_ips(NetworkInterface::show().unwrap());
        info!("Found IPs: {:?}", ips);

        for ip in ips.iter() {
            info!("Testing IP: {:?}", ip);

            match self.test_for_doip(ip).await {
                Ok(stream) => {
                    trace!("Discover Doip Networks (Return): {:?}", &stream);
                    return Ok(stream);
                }
                Err(e) => {
                    error!("Error (IP: {:?}): {:?} ", ip, e);
                    continue;
                }
            };
        }

        error!("No IP addresses found");
        Err(DoipDiscoveryError::DoipDiscovery(
            DoipDiscovery::NoNetworkFound,
        ))
    }

    async fn setup_doip_tester_socket(
        &mut self,
        addr: &SocketAddr,
    ) -> Result<UdpSocket, TestForDoipError> {
        trace!("Setup Doip Tester Socket (Init): {:?}", &addr);
        // Bind UDP Socket to address
        let sock = match UdpSocket::bind(addr).await {
            Ok(sock) => sock,
            Err(e) => return Err(TestForDoipError::Io(e)),
        };

        // Set broadcast option
        let _ = sock.set_broadcast(true);
        let _ = sock.set_ttl(255);

        trace!("Setup Doip Tester Socket (Return): {:?}", &sock);
        Ok(sock)
    }

    async fn test_for_doip(&mut self, addr: &SocketAddr) -> Result<TcpStream, TestForDoipError> {
        trace!("Test for Doip (Init): {:?}", &addr);
        let gateway = match self.get_gateway(addr).await {
            Ok(gateway) => gateway,
            Err(err) => return Err(err),
        };

        let sock = TcpSocket::new_v4().unwrap();

        let mut gateway_stream = match sock.connect(gateway.address).await {
            Ok(stream) => stream,
            Err(e) => return Err(TestForDoipError::Io(e)),
        };

        gateway_stream.set_nodelay(true).unwrap();

        let _rar = match self.get_routing_authentication(&mut gateway_stream).await {
            Ok(rar) => rar,
            Err(err) => return Err(err),
        };

        let _ = sleep(Duration::from_millis(100)).await;

        let nodes = match self.get_edge_nodes(addr).await {
            Ok(nodes) => nodes,
            Err(err) => return Err(err),
        };

        self.nodes.extend(nodes);
        self.gateway = gateway;

        trace!("Test for Doip (Return): {:?}", &gateway_stream);
        Ok(gateway_stream)
    }

    async fn get_routing_authentication(
        &self,
        stream: &mut TcpStream,
    ) -> Result<RoutingActivationResponse, TestForDoipError> {
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
                return Err(TestForDoipError::Io(e));
            }
        };

        let res = &buffer[..bytes];
        let msgs = match DoipMessage::parse_from_bytes(res.to_vec()) {
            Ok(msgs) => msgs,
            Err(e) => {
                error!("Get Routing Authentication (Message Parse): {:?}", e);
                return Err(TestForDoipError::Parse(e));
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
                        return Err(TestForDoipError::Parse(
                            ParseError::FailedAuthenticationCheck,
                        ));
                    }
                },
                None => {
                    error!("Get Routing Authentication (Routing Activation Response Parse Failed)");
                    continue;
                }
            };
        }

        Err(TestForDoipError::Parse(
            ParseError::FailedToGetAuthentication,
        ))
    }

    fn filter_network_ips(&self, nis: Vec<NetworkInterface>) -> Vec<SocketAddr> {
        trace!("Filter Network IPs (Init): {:?}", &nis);
        const NETWORK_INTERFACE_PREFIX: &str = "169.254";
        let mut ips: Vec<SocketAddr> = Vec::new();
        info!("All IPs: {:?}", nis);

        for itf in nis.iter() {
            // if !addr_contains_prefix(&itf.addr.get(0).unwrap(), NETWORK_INTERFACE_PREFIX) {
            //     continue;
            // };

            for addr in itf.addr.iter() {
                // if !addr_contains_prefix(addr, NETWORK_INTERFACE_PREFIX) {
                //     continue;
                // };

                ips.push(SocketAddr::new(addr.ip(), 13400));
            }
        }
        trace!("Filter Network IPs (Return): {:?}", &ips);
        ips
    }

    fn doip_message_from_responses(
        &self,
        responses: &Vec<(SocketAddr, Vec<u8>)>,
    ) -> Vec<(SocketAddr, DoipMessage)> {
        trace!("Doip Message From Responses (Init): {:?}", &responses);
        let mut msgs: Vec<(SocketAddr, DoipMessage)> = vec![];

        for (addr, bytes) in responses {
            match DoipMessage::parse_from_bytes(bytes.to_vec()) {
                Ok(msg) => {
                    for m in msg {
                        msgs.push((*addr, m));
                    }
                }
                Err(_) => continue,
            }
        }

        trace!("Doip Message From Responses (Return): {:?}", &msgs);
        msgs
    }

    async fn get_responses(
        &self,
        sock: &UdpSocket,
    ) -> Result<Vec<(SocketAddr, Vec<u8>)>, TestForDoipError> {
        trace!("Get Responses (Init): {:?}", sock);
        let mut buffer = [0; 4096];
        let mut responses: Vec<(SocketAddr, Vec<u8>)> = Vec::new();

        let duration = Duration::from_millis(200);
        let start_time = Instant::now();

        while start_time.elapsed() < duration {
            // Use timeout to ensure we wait for incoming packets within the remaining time window
            match time::timeout(duration - start_time.elapsed(), sock.recv_from(&mut buffer)).await
            {
                Ok(Ok((len, addr))) => {
                    // Successfully received data
                    trace!("Get Responses (Timeout): {:?}", buffer[..len].to_vec());
                    responses.push((addr, buffer[..len].to_vec()));
                }
                Ok(Err(e)) => {
                    eprintln!("Error receiving data: {:?}", e);
                    break;
                }
                Err(_) => {
                    // Timeout elapsed without receiving data
                    break;
                }
            }
        }
        trace!("Get Responses (Return): {:?}", &responses);
        Ok(responses)
    }

    fn filter_vam(
        &self,
        bytes_from: &Vec<(SocketAddr, Vec<u8>)>,
    ) -> Vec<(SocketAddr, VehicleAnnouncementMessage)> {
        trace!("Filter VAM (Init): {:?}", &bytes_from);
        let b = bytes_from
            .iter()
            .filter_map(|(addr, bytes)| {
                let msgs = match DoipMessage::parse_from_bytes(bytes.to_vec()) {
                    Ok(msgs) => msgs,
                    Err(_) => return None,
                };

                let vams = msgs.into_iter().find(|msg| {
                    matches!(
                        msg.header.payload_type,
                        PayloadType::VehicleAnnouncementMessage
                    )
                });
                vams.and_then(|msg| {
                    VehicleAnnouncementMessage::from_bytes(&msg.payload.to_bytes())
                        .map(|vam| (*addr, vam))
                })
            })
            .collect();

        trace!("Filter VAM (Return): {:?}", &b);
        b
    }

    async fn send_entity_status_request(
        &self,
        sock: &UdpSocket,
        addr: &SocketAddr,
    ) -> Vec<(SocketAddr, EntityStatusResponse)> {
        trace!(
            "Send Entity Status Request (Init): {:?} | {:?}",
            &sock,
            &addr
        );
        let entity_req =
            DoipMessage::new(DoipVersion::Iso13400_2012, Box::new(EntityStatusRequest {}));

        let _ = sock.set_ttl(255);
        let _ = sock.send_to(&entity_req.to_bytes(), addr).await;

        let responses = match self.get_responses(sock).await {
            Ok(res) => res,
            Err(_) => return vec![],
        };

        let res = self
            .doip_message_from_responses(&responses)
            .iter()
            .filter_map(|(addr, msg)| {
                EntityStatusResponse::from_bytes(&msg.payload.to_bytes()).map(|esr| (*addr, esr))
            })
            .collect();

        trace!("Send Entity Status Request (Return): {:?}", &res);
        res
    }

    fn filter_nodes_by_type(
        &mut self,
        vams: &Vec<(SocketAddr, VehicleAnnouncementMessage)>,
        responses: Vec<(SocketAddr, EntityStatusResponse)>,
    ) -> Vec<DoipNode> {
        trace!(
            "Filter Nodes By Type (Init): {:?} | {:?}",
            &vams,
            &responses
        );
        let mut nodes: HashSet<DoipNode> = HashSet::new();

        // Create a HashMap for quick lookup of responses by SocketAddr
        let response_map: HashMap<SocketAddr, EntityStatusResponse> =
            responses.into_iter().collect();

        for (addr, vam) in vams {
            if let Some(ent_res) = response_map.get(addr) {
                match ent_res.node_type {
                    NodeType::DoipNode => {
                        nodes.insert(DoipNode::from_res(*ent_res, vam.logical_address, *addr));
                    }
                    NodeType::DoipGateway => {
                        self.gateway = DoipGateway::from_res(*ent_res, vam.logical_address, *addr);
                    }
                }
            } else {
                if vam.logical_address == self.gateway.logical_address {
                    continue;
                }

                nodes.insert(DoipNode {
                    currently_open_sockets: [0],
                    max_concurrent_sockets: [1],
                    max_data_size: [0x00, 0x00, 0xff, 0xff],
                    address: *addr,
                    logical_address: vam.logical_address,
                });
            }
        }
        let node_vec: Vec<_> = nodes.into_iter().collect();

        trace!("Filter Nodes By Type (Return): {:?}", &node_vec);
        node_vec
    }

    async fn get_edge_nodes(
        &mut self,
        addr: &SocketAddr,
    ) -> Result<Vec<DoipNode>, TestForDoipError> {
        trace!("Get Edge Nodes (Init): {:?}", &addr);
        let (sock, vams) = self.send_vehicle_identification_request(addr).await?;

        let mut nodes: HashSet<DoipNode> = HashSet::new();

        for (addr, vam) in vams.iter() {
            if vam.logical_address == self.gateway.logical_address {
                continue;
            }

            let responses = self.send_entity_status_request(&sock, addr).await;
            nodes.extend(self.filter_nodes_by_type(&vams, responses));
        }

        if nodes.is_empty() {
            error!(
                "Get Edge Nodes: {:?}",
                TestForDoipError::Parse(ParseError::NoEdgeNodes)
            );
        }

        let mut seen_addresses = HashSet::new();
        trace!("{:?}", &nodes);

        let nodes_vec: Vec<_> = nodes
            .into_iter()
            .filter(|node| seen_addresses.insert(node.logical_address))
            .filter(|node| node.logical_address != self.gateway.logical_address)
            .collect();

        trace!("{:?}", &seen_addresses);

        trace!("Get Edge Nodes (Return): {:?}", &nodes_vec);
        Ok(nodes_vec)
    }

    async fn get_gateway(&mut self, addr: &SocketAddr) -> Result<DoipGateway, TestForDoipError> {
        trace!("Get Gateway (Init): {:?}", &addr);
        let (sock, vams) = self.send_vehicle_identification_request(addr).await?;

        for (addr, vam) in vams.iter() {
            let responses = self.send_entity_status_request(&sock, addr).await;

            trace!("Get Gateway (Responses): {:?}", &responses);
            for (addr, ent_res) in responses.iter() {
                if ent_res.node_type == NodeType::DoipGateway {
                    let gate = DoipGateway::from_res(*ent_res, vam.logical_address, *addr);
                    self.vehicle.detect_architecture(vam);
                    self.vehicle.vin = vam.vin;

                    trace!("Get Gateway (Return): {:?}", &gate);
                    return Ok(gate);
                }
            }
        }

        Err(TestForDoipError::Parse(ParseError::GatewayNotAnnouncing))
    }

    async fn send_vehicle_identification_request(
        &mut self,
        addr: &SocketAddr,
    ) -> Result<(UdpSocket, Vec<(SocketAddr, VehicleAnnouncementMessage)>), TestForDoipError> {
        trace!("Send Vehicle Identitifcation Request (Init): {:?}", &addr);
        let sock = match self.setup_doip_tester_socket(addr).await {
            Ok(sock) => sock,
            Err(e) => return Err(e),
        };

        // Declare Broadcast Address
        const BROADCAST_ADDRESS: SocketAddr =
            SocketAddr::new(IpAddr::V4(Ipv4Addr::new(255, 255, 255, 255)), 13400);

        let vir = DoipMessage::new(
            DoipVersion::Iso13400_2012,
            Box::new(VehicleIdentificationRequest {}),
        );

        let _ = sock.send_to(&vir.to_bytes(), BROADCAST_ADDRESS).await;
        let _ = sock.send_to(&vir.to_bytes(), BROADCAST_ADDRESS).await;

        let responses = match self.get_responses(&sock).await {
            Ok(res) => res,
            Err(err) => return Err(err),
        };

        let vams = self.filter_vam(&responses);
        trace!("Send Vehicle Identification Request (VAMS): {:?}", &vams);

        trace!(
            "Send Vehicle Identitifcation Request (Return): {:?} | {:?}",
            &addr,
            &vams
        );
        Ok((sock, vams))
    }
}

impl Default for Client {
    fn default() -> Self {
        Self {
            nodes: Vec::new(),
            gateway: DoipGateway::new(),
            vehicle: Vehicle::new(),
            host: Host::new(),
        }
    }
}

fn addr_contains_prefix(addr: &Addr, prefix: &str) -> bool {
    addr.ip().to_string().contains(prefix)
}
