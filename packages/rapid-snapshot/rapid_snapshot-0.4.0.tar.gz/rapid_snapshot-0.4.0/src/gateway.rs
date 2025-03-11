use log::trace;
use tokio::{
    net::tcp::{OwnedReadHalf, OwnedWriteHalf},
    sync::Mutex,
};

use crate::{
    architecture::JlrArchitecture,
    doip::{
        header::payload::entity_status_response::EntityStatusResponse, message::node_type::NodeType,
    },
    entity::DoipEntity,
    error::DoipSnapshotError,
    output::ECUOutput,
    snapshot::{DoipSnapshot, Snapshot},
};
use std::{
    net::{IpAddr, Ipv4Addr, SocketAddr},
    sync::Arc,
};

#[derive(Clone, Debug)]
pub struct DoipGateway {
    pub currently_open_sockets: [u8; 1],
    pub max_concurrent_sockets: [u8; 1],
    pub max_data_size: [u8; 4],
    pub address: SocketAddr,
    pub logical_address: [u8; 2],
}

impl DoipGateway {
    pub fn new() -> Self {
        DoipGateway::default()
    }

    pub fn from_res(
        msg: EntityStatusResponse,
        logical_address: [u8; 2],
        address: SocketAddr,
    ) -> Self {
        Self {
            currently_open_sockets: msg.currently_open_sockets,
            max_concurrent_sockets: msg.max_concurrent_sockets,
            max_data_size: msg.max_data_size,
            address,
            logical_address,
        }
    }
}

impl Default for DoipGateway {
    fn default() -> Self {
        Self {
            currently_open_sockets: [0; 1],
            max_concurrent_sockets: [0; 1],
            max_data_size: [0; 4],
            address: SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080),
            logical_address: [0; 2],
        }
    }
}

impl DoipEntity for DoipGateway {
    async fn snapshot(
        &mut self,
        arch: JlrArchitecture,
        stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<Vec<ECUOutput>, DoipSnapshotError> {
        trace!("Gateway Snapshot (Init): {:?} | {:?}", &arch, &stream);
        let snapshot = Snapshot::new(
            NodeType::DoipGateway,
            &self.address,
            self.logical_address,
            arch,
        )
        .await;
        let output = snapshot.snapshot(stream).await;

        trace!("Gateway Snapshot (Return): {:?}", &output);
        output
    }
}
