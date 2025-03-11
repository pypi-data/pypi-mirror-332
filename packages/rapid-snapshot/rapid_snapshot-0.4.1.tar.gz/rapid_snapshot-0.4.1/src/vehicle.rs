use crate::{
    architecture::JlrArchitecture,
    doip::header::payload::vehicle_announcement_message::VehicleAnnouncementMessage,
};

#[derive(Clone, Debug)]
pub struct Vehicle {
    pub vin: [u8; 17],
    pub architecture: JlrArchitecture,
}

impl Vehicle {
    pub fn new() -> Self {
        Vehicle::default()
    }

    pub fn detect_architecture(&mut self, vam: &VehicleAnnouncementMessage) {
        self.architecture = JlrArchitecture::new(vam);
    }
}

impl Default for Vehicle {
    fn default() -> Self {
        Self {
            vin: [
                95, 95, 95, 95, 95, 95, 95, 118, 105, 110, 95, 95, 95, 95, 95, 95, 95,
            ],
            architecture: JlrArchitecture::Unknown,
        }
    }
}
