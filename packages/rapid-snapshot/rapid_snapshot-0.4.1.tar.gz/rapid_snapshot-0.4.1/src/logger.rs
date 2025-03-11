use std::path::{Path, PathBuf};

use log::LevelFilter;
use tokio::fs;
use uuid::Uuid;

pub async fn program_preconditions() -> PathBuf {
    let log_path = format!("C:\\Users\\{}\\AppData\\Local\\PST\\", whoami::username());

    // Convert the `log_path` string to a `PathBuf` so we can return an owned value.
    let path = PathBuf::from(&log_path);

    // Check if the path exists, and if not, create it.
    if !path.exists() {
        fs::create_dir(&path).await.unwrap();
    }

    path // Return the PathBuf, which owns the path
}

pub fn setup_logging(
    path: &Path,
    log_level: LevelFilter,
) -> Result<(), Box<dyn std::error::Error>> {
    // Generate unique id using UUIDv4
    let id = Uuid::new_v4();

    let version = env!("CARGO_PKG_VERSION").replace(".", "_");

    // Format this into a simple 8 character long string appended with _parallel.log
    let log_name = format!("{}_rst_{}.log", &id.to_string()[0..8], version);

    fern::Dispatch::new()
        .format(|out, message, record| {
            out.finish(format_args!(
                "[{} {} {}] {}",
                humantime::format_rfc3339(std::time::SystemTime::now()),
                record.level(),
                record.target(),
                message
            ))
        })
        .level(log_level)
        .chain(fern::DateBased::new(path, log_name))
        .apply()?;

    Ok(())
}
