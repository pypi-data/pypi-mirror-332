use std::time::{Duration, SystemTime, UNIX_EPOCH};

#[derive(Debug, Clone)]
pub struct Host {
    pub hostname: String,
    pub exec_start: Duration,
}

impl Host {
    pub fn new() -> Self {
        Self {
            hostname: hostname::get().unwrap().into_string().unwrap(),
            exec_start: SystemTime::now().duration_since(UNIX_EPOCH).unwrap(),
        }
    }
}
