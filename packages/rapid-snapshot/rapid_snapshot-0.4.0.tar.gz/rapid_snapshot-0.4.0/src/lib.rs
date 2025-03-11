use args::{LogLevel, SnapshotArgs};
use clap::Parser;
use pyo3::{
    exceptions::{PyIOError, PyValueError},
    prelude::*,
};

use client::Client;
use error::DoipSnapshotError;
use log::LevelFilter;
use logger::{program_preconditions, setup_logging};
use tokio::{runtime::Runtime, time::Instant};
use updater::update_self;

mod architecture;
mod args;
mod client;
mod did;
mod doip;
mod ecu;
mod entity;
mod error;
mod gateway;
mod host;
mod logger;
mod node;
mod output;
mod snapshot;
mod updater;
mod utils;
mod vehicle;

#[derive(Clone)]
#[pyclass]
pub struct PySnapshotArgs {
    pub custom_path: Option<std::path::PathBuf>,
    pub log_level: LogLevel,
    pub delay: u16,
}

#[pymethods]
impl PySnapshotArgs {
    // Constructor for SnapshotArgs
    #[new]
    fn new(custom_path: Option<std::path::PathBuf>, log_level: LogLevel, delay: u16) -> Self {
        PySnapshotArgs {
            custom_path,
            log_level,
            delay,
        }
    }
}

impl IntoIterator for PySnapshotArgs {
    type Item = String;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        let mut args = vec![];

        if let Some(path) = self.custom_path {
            args.push(format!("--custom-path={}", path.to_string_lossy()));
        }

        args.push(format!("--log-level={}", self.log_level));

        args.push(format!("--delay={}", self.delay));

        args.into_iter()
    }
}

#[pyfunction]
#[pyo3(signature=(args))]
fn snapshot_vehicle_sync(args: PySnapshotArgs) -> PyResult<()> {
    // Create a new Tokio runtime explicitly
    let rt = Runtime::new().map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Failed to create Tokio runtime: {}", e)))?;

    // Run the async function within this runtime
    rt.block_on(async {
        snapshot_vehicle(args).await?;
        Ok(())
    })
}

#[pyfunction]
#[pyo3(signature=(args))]
pub async fn snapshot_vehicle(args: PySnapshotArgs) -> Result<(), DoipSnapshotError> {
    let args = SnapshotArgs::parse_from(args);

    if let Some(target_version) = args.update {
        let _ = update_self(&target_version).await;
        return Ok(());
    };

    let log_level = match args.log_level {
        args::LogLevel::Off => LevelFilter::Off,
        args::LogLevel::Error => LevelFilter::Error,
        args::LogLevel::Warn => LevelFilter::Warn,
        args::LogLevel::Info => LevelFilter::Info,
        args::LogLevel::Debug => LevelFilter::Debug,
        args::LogLevel::Trace => LevelFilter::Trace,
        args::LogLevel::Max => LevelFilter::max(),
    };

    // Logging
    let path = program_preconditions().await;
    setup_logging(&path, log_level).expect("Failed to initialize logging.");

    let now = Instant::now();
    // Begin Snapshot
    let mut cli = Client::new();
    let _ = cli.snapshot().await?;

    let elapsed = now.elapsed().as_nanos();
    println!("Snapshot took: {:.2?} nanoseconds", elapsed);

    Ok(())
}

#[pymodule]
fn rapid_snapshot(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_function(wrap_pyfunction!(snapshot_vehicle_sync, m)?);
    let _ = m.add_class::<PySnapshotArgs>()?;
    let _ = m.add_class::<LogLevel>()?;

    Ok(())
}

/// Convert `DoipSnapshotError` into a Python exception (`PyErr`)
impl From<DoipSnapshotError> for PyErr {
    fn from(err: DoipSnapshotError) -> PyErr {
        match err {
            DoipSnapshotError::Io(e) => PyIOError::new_err(format!("IO Error: {}", e)),
            DoipSnapshotError::Snapshot(e) => PyValueError::new_err(format!("Snapshot Error: {}", e)),
        }
    }
}
