use clap::Parser;
use client::Client;
use log::LevelFilter;
use logger::{program_preconditions, setup_logging};
use tokio::time::Instant;
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

use args::SnapshotArgs;

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let args = SnapshotArgs::parse();

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
    let res = cli.snapshot().await;

    match res {
        Ok(_success) => println!("Successfully completed."),
        Err(err) => println!("Error: {:?}", err),
    }

    let elapsed = now.elapsed().as_nanos();
    println!("Snapshot took: {:.2?} nanoseconds", elapsed);

    Ok(())
}
