use std::{
    net::{IpAddr, Ipv4Addr, SocketAddr},
    sync::Arc,
};

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
    error::{DoipSnapshotError, SnapshotError},
    output::ECUOutput,
    snapshot::{DoipSnapshot, Snapshot},
};

#[derive(Clone, Debug, Eq, Hash, PartialEq)]
pub struct DoipNode {
    pub currently_open_sockets: [u8; 1],
    pub max_concurrent_sockets: [u8; 1],
    pub max_data_size: [u8; 4],
    pub address: SocketAddr,
    pub logical_address: [u8; 2],
}

impl DoipNode {
    pub fn _new() -> Self {
        DoipNode::default()
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

impl Default for DoipNode {
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

impl DoipEntity for DoipNode {
    async fn snapshot(
        &mut self,
        arch: JlrArchitecture,
        _stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<Vec<ECUOutput>, DoipSnapshotError> {
        trace!("Node Snapshot (Init): {:?}", &arch);
        let snapshot = Snapshot::new(
            NodeType::DoipNode,
            &self.address,
            self.logical_address,
            arch,
        )
        .await;

        if self.currently_open_sockets >= self.max_concurrent_sockets {
            return Err(DoipSnapshotError::Snapshot(
                SnapshotError::MaxSocketsConnected,
            ));
        }

        if snapshot.snapshot_ecus.is_empty() {
            return Err(DoipSnapshotError::Snapshot(SnapshotError::NodeNotRequired));
        }

        let output = snapshot.snapshot(None).await;

        trace!("Node Snapshot (Return): {:?}", &output);
        output
    }
}
