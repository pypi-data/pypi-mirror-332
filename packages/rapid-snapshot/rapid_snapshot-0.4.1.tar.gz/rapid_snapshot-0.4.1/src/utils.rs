use std::fmt::Write;

use clap::Parser;
use log::error;
use serde_json::Value;
use tokio::{fs::File, io::AsyncReadExt};

use crate::{
    architecture::JlrArchitecture, args::SnapshotArgs, did::Did, ecu::SnapshotEcu,
    error::CustomInputParserError,
};

pub fn _hex_string_to_bytes(hex_string: &str) -> Vec<u8> {
    (0..hex_string.len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&hex_string[i..i + 2], 16).unwrap())
        .collect()
}
pub fn _hex_to_char(s: &str) -> Result<char, std::num::ParseIntError> {
    u8::from_str_radix(s, 16).map(|n| n as char)
}

pub fn bytes_to_ascii(bytes: &[u8]) -> Result<String, String> {
    match String::from_utf8(bytes.to_vec()) {
        Ok(ascii) => Ok(ascii),
        Err(_) => Err("Invalid UTF-8 sequence".to_string()),
    }
}

pub fn bytes_to_hex_string(bytes: &[u8]) -> String {
    bytes.iter().fold(String::new(), |mut output, b| {
        let _ = write!(output, "{b:02X}");
        output
    })
}

pub fn parse_custom_input(str: Value) -> Result<Vec<SnapshotEcu>, CustomInputParserError> {
    let array = str
        .as_array()
        .ok_or(CustomInputParserError::JsonTypeError)?;

    let mut ecus = Vec::new();

    for ecu in array {
        let name = ecu
            .get("name")
            .and_then(|v| v.as_str())
            .ok_or_else(|| CustomInputParserError::MissingField("name".to_string()))?;

        let acronym = ecu
            .get("acronym")
            .and_then(|v| v.as_str())
            .ok_or_else(|| CustomInputParserError::MissingField("acronym".to_string()))?;

        let logical_address = ecu
            .get("logical_address")
            .and_then(|v| v.as_str())
            .ok_or_else(|| CustomInputParserError::MissingField("logical_address".to_string()))?;

        if logical_address.len() != 4 {
            return Err(CustomInputParserError::InvalidField(
                "logical_address must be 4 hex characters".to_string(),
            ));
        }

        let address = [
            u8::from_str_radix(&logical_address[0..2], 16)
                .map_err(|_| CustomInputParserError::InvalidField("logical_address".to_string()))?,
            u8::from_str_radix(&logical_address[2..4], 16)
                .map_err(|_| CustomInputParserError::InvalidField("logical_address".to_string()))?,
        ];

        let architecture = ecu
            .get("architecture")
            .and_then(|v| v.as_array())
            .ok_or_else(|| CustomInputParserError::MissingField("architecture".to_string()))?
            .iter()
            .map(|arch| match arch.as_str() {
                Some("eva2") => Ok(JlrArchitecture::Eva2),
                Some("eva25") => Ok(JlrArchitecture::Eva25),
                _ => Err(CustomInputParserError::InvalidField(
                    "architecture contains an unknown value".to_string(),
                )),
            })
            .collect::<Result<Vec<JlrArchitecture>, CustomInputParserError>>()?;

        let dids_array = ecu
            .get("dids")
            .and_then(|v| v.as_array())
            .ok_or_else(|| CustomInputParserError::MissingField("dids".to_string()))?;

        let mut dids = Vec::new();

        for did in dids_array {
            let name = did
                .get("name")
                .and_then(|v| v.as_str())
                .ok_or_else(|| CustomInputParserError::MissingField("dids.name".to_string()))?;

            let did_value = did
                .get("did")
                .and_then(|v| v.as_str())
                .ok_or_else(|| CustomInputParserError::MissingField("dids.did".to_string()))?;

            if did_value.len() != 4 {
                return Err(CustomInputParserError::InvalidField(
                    "dids.did must be 4 hex characters".to_string(),
                ));
            }

            let did = [
                u8::from_str_radix(&did_value[0..2], 16)
                    .map_err(|_| CustomInputParserError::InvalidField("dids.did".to_string()))?,
                u8::from_str_radix(&did_value[2..4], 16)
                    .map_err(|_| CustomInputParserError::InvalidField("dids.did".to_string()))?,
            ];

            dids.push(Did {
                name: name.to_string(),
                did,
            });
        }

        ecus.push(SnapshotEcu {
            name: name.to_string(),
            acronym: acronym.to_string(),
            address,
            architecture,
            dids,
        });
    }

    Ok(ecus)
}

pub async fn get_custom_input() -> Result<Vec<SnapshotEcu>, CustomInputParserError> {
    let args = SnapshotArgs::parse();

    Ok(match args.custom_path {
        Some(path) => match File::open(path).await {
            Ok(mut file) => {
                let mut file_contents = String::new();
                match file.read_to_string(&mut file_contents).await {
                    Ok(_) => match serde_json::from_str::<serde_json::Value>(&file_contents) {
                        Ok(json) => match parse_custom_input(json) {
                            Ok(ecus) => ecus,
                            Err(e) => {
                                error!("Custom ECU Parsing: {:?}", e);
                                return Err(e);
                            }
                        },
                        Err(err) => {
                            error!("Failed to parse JSON: {}", err);
                            return Err(CustomInputParserError::JsonParseError(err));
                        }
                    },
                    Err(err) => {
                        error!("Failed to read file: {}", err);
                        return Err(CustomInputParserError::OpenFileError(err));
                    }
                }
            }
            Err(err) => {
                error!("Failed to open file: {}", err);
                return Err(CustomInputParserError::OpenFileError(err));
            }
        },
        _ => {
            error!("No path provided.");
            return Err(CustomInputParserError::NoPath);
        }
    })
}
