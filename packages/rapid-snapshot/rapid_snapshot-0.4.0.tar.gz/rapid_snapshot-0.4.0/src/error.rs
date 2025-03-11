#![allow(dead_code)]
// use std::{error::Error, fmt};

// #[derive(Debug)]
// pub struct DoipNetworkNotFound {}

// #[derive(Debug)]
// pub enum GatewayConnectionError {
//     DoipNetworkNotFound,
//     UnableToBindSocket,
//     ReadError,
//     ReadTimeout,
//     InvalidResponse,
//     DoipNetworkNotGateway,
//     EntityError,
//     GatewayTcpNotConnected,
// }

// #[derive(Debug)]
// pub enum RoutingActivationError {
//     NoDoipGatewayAvailable,
//     GatewayTcpNotConnected,
//     ReadError,
//     NotRoutingActivationResponse,
//     FailedToAuthenticate(ActivationCode),
// }

// #[derive(Debug)]
// pub enum TcpStreamConnectionError {
//     TcpAlreadyActive,
//     TcpLimitReached,
// }

// #[derive(Debug)]
// pub enum SnapshotError {
//     NoDoipGatewayAvailable,
//     GatewayTcpNotConnected,
// }

use std::{fmt, io};

#[derive(Debug)]
pub enum ParseError {
    EmptyInput,
    InvalidProtocolVersion,
    FailedProtocolCheck,
    PayloadNotRecognised,
    InvalidPayloadData,
    UnsupportedPayloadType,
    FailedAuthenticationCheck,
    FailedToGetAuthentication,
    TimedOut,
    GatewayNotAnnouncing,
    NoEdgeNodes,
}

#[derive(Debug)]
pub enum TestForDoipError {
    Io(io::Error),
    Parse(ParseError),
}

// Implement the `std::fmt::Display` trait for your custom error
impl fmt::Display for TestForDoipError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            TestForDoipError::Io(e) => write!(f, "IO error: {}", e),
            TestForDoipError::Parse(e) => write!(f, "Parse error: {}", e),
        }
    }
}

// Implement the `std::error::Error` trait for your custom error
impl std::error::Error for TestForDoipError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            TestForDoipError::Io(e) => Some(e),
            TestForDoipError::Parse(e) => Some(e),
        }
    }
}

// Implement `From` to allow automatic conversion from `io::Error` to `TestForDoipError`
impl From<io::Error> for TestForDoipError {
    fn from(err: io::Error) -> Self {
        TestForDoipError::Io(err)
    }
}

// Implement `From` to allow automatic conversion from `ParseError` to `TestForDoipError`
impl From<ParseError> for TestForDoipError {
    fn from(err: ParseError) -> Self {
        TestForDoipError::Parse(err)
    }
}

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "An error occurred during parsing ParseError")
    }
}

impl std::error::Error for ParseError {}

#[derive(Debug)]
pub enum SnapshotError {
    FailedAuthenticationCheck,
    FailedToGetAuthentication,
    MaxSocketsConnected,
    NoGatewayStream,
    ParsingError(ParseError),
    DiscoveryError(DoipDiscoveryError),
    StreamNotRecovered,
    StreamReuniteError,
    ArcUnwrapFailed,
    NodeNotRequired,
}

#[derive(Debug)]
pub enum DoipSnapshotError {
    Io(io::Error),
    Snapshot(SnapshotError),
}

// Implement the `std::fmt::Display` trait for your custom error
impl fmt::Display for DoipSnapshotError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            DoipSnapshotError::Io(e) => write!(f, "IO error: {}", e),
            DoipSnapshotError::Snapshot(e) => write!(f, "Snapshot error: {}", e),
        }
    }
}

// Implement the `std::error::Error` trait for your custom error
impl std::error::Error for DoipSnapshotError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            DoipSnapshotError::Io(e) => Some(e),
            DoipSnapshotError::Snapshot(e) => Some(e),
        }
    }
}

// Implement `From` to allow automatic conversion from `io::Error` to `DoipSnapshotError`
impl From<io::Error> for DoipSnapshotError {
    fn from(err: io::Error) -> Self {
        DoipSnapshotError::Io(err)
    }
}

// Implement `From` to allow automatic conversion from `DoipSnapshotError` to `DoipSnapshotError`
impl From<SnapshotError> for DoipSnapshotError {
    fn from(err: SnapshotError) -> Self {
        DoipSnapshotError::Snapshot(err)
    }
}

impl fmt::Display for SnapshotError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "An error occurred during parsing SnapshotError")
    }
}

impl std::error::Error for SnapshotError {}

#[derive(Debug)]
pub enum DoipDiscovery {
    NoNetworkFound,
}

#[derive(Debug)]
pub enum DoipDiscoveryError {
    Io(io::Error),
    DoipDiscovery(DoipDiscovery),
}

// Implement the `std::fmt::Display` trait for your custom error
impl fmt::Display for DoipDiscoveryError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            DoipDiscoveryError::Io(e) => write!(f, "IO error: {}", e),
            DoipDiscoveryError::DoipDiscovery(e) => write!(f, "Doip Discovery error: {}", e),
        }
    }
}

// Implement the `std::error::Error` trait for your custom error
impl std::error::Error for DoipDiscoveryError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            DoipDiscoveryError::Io(e) => Some(e),
            DoipDiscoveryError::DoipDiscovery(e) => Some(e),
        }
    }
}

// Implement `From` to allow automatic conversion from `io::Error` to `DoipDiscoveryError`
impl From<io::Error> for DoipDiscoveryError {
    fn from(err: io::Error) -> Self {
        DoipDiscoveryError::Io(err)
    }
}

// Implement `From` to allow automatic conversion from `DoipDiscovery` to `DoipDiscoveryError`
impl From<DoipDiscovery> for DoipDiscoveryError {
    fn from(err: DoipDiscovery) -> Self {
        DoipDiscoveryError::DoipDiscovery(err)
    }
}

impl fmt::Display for DoipDiscovery {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "An error occurred during doip discovery")
    }
}

impl std::error::Error for DoipDiscovery {}

#[derive(Debug)]
pub enum CustomInputParserError {
    JsonTypeError,
    InvalidPath,
    JsonParseError(serde_json::Error),
    OpenFileError(std::io::Error),
    MissingField(String),
    InvalidField(String),
    NoPath,
}

impl fmt::Display for CustomInputParserError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "An error occurred during parsing custom input")
    }
}

impl std::error::Error for CustomInputParserError {}
