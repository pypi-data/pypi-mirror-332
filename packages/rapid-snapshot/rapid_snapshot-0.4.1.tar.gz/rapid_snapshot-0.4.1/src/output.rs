use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct OutFileBase {
    pub vin: String,
    pub distance: i64,
    pub voltage: i64,
    pub interior_temperature: i64,
    pub exterior_temperature: i64,
    pub power_mode: i64,
    pub ecus: Vec<ECUOutput>,
    pub version: String,
    pub time_taken: u128
}

impl OutFileBase {
    pub fn _new() -> Self {
        OutFileBase {
            vin: String::new(),
            distance: 0,
            voltage: 0,
            interior_temperature: 0,
            exterior_temperature: 0,
            power_mode: 0,
            ecus: Vec::<ECUOutput>::new(),
            version: String::new(),
            time_taken: 0
        }
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct DIDOutput {
    pub did: String,
    pub name: String,
    pub response: Response,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Response {
    pub ascii: String,
    pub hex: String,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct DTCOutput {
    hex: String,
    code: String,
    severity: String,
    description: String,
    extended: DTCExtendedOutput,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
struct DTCExtendedOutput {
    cycle_since_last_detected: i64,
    cycle_since_first_detected: i64,
    cycles_which_detected: i64,
    detection_counter: i64,
    response: Response,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct ECUOutput {
    pub name: String,
    pub acronym: String,
    pub address: String,
    pub dids: Vec<DIDOutput>,
    pub dtcs: Vec<DTCOutput>,
}
