use std::sync::Arc;

use tokio::{
    net::tcp::{OwnedReadHalf, OwnedWriteHalf},
    sync::Mutex,
};

use crate::{architecture::JlrArchitecture, error::DoipSnapshotError, output::ECUOutput};

pub trait DoipEntity {
    async fn snapshot(
        &mut self,
        arch: JlrArchitecture,
        stream: Option<(Arc<Mutex<OwnedReadHalf>>, Arc<Mutex<OwnedWriteHalf>>)>,
    ) -> Result<Vec<ECUOutput>, DoipSnapshotError>;
}
