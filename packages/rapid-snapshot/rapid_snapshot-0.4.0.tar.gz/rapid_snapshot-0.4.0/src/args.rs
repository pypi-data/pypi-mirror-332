use clap::{Parser, ValueEnum};
use pyo3::pyclass;

#[derive(Debug, Parser, Clone)]
#[clap(author, version, about)]
pub struct SnapshotArgs {
    #[clap(
        long,
        short = 'x',
        help = "Path to the custom input file. For example: 'static/example-input.json'"
    )]
    pub custom_path: Option<std::path::PathBuf>,
    #[clap(
        long,
        short = 'l',
        value_enum,
        default_value = "error",
        help = "Set the logging level"
    )]
    pub log_level: LogLevel,
    #[clap(
        long,
        short = 'd',
        default_value = "1",
        help = "Delay in milliseconds between request (MAX: 65535)"
    )]
    pub delay: u16,
    #[arg(long, help = "Update to a specific version")]
    pub update: Option<String>,
}

#[pyclass]
#[derive(Debug, Clone, ValueEnum)]
pub enum LogLevel {
    /// No Logs are recorded
    Off,
    /// Only Error logs are recorded
    Error,
    /// Warn and Error logs are recorded
    Warn,
    /// Error, Warn, and Info logs are recorded
    Info,
    /// Error, Warn, Info, and Debug logs are recorded
    Debug,
    /// Error, Warn, Info, Debug, and Trace logs are recorded
    Trace,
    /// All logs are recorded
    Max,
}

impl std::fmt::Display for LogLevel {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let level_str = match self {
            LogLevel::Off => "off",
            LogLevel::Error => "error",
            LogLevel::Warn => "warn",
            LogLevel::Info => "info",
            LogLevel::Debug => "debug",
            LogLevel::Trace => "trace",
            LogLevel::Max => "max",
        };
        write!(f, "{}", level_str)
    }
}
