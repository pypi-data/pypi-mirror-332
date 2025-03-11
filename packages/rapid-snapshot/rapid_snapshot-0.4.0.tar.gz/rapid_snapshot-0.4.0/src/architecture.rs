use crate::{
    doip::header::payload::vehicle_announcement_message::VehicleAnnouncementMessage,
    ecu::{create_ecu_list, Ecu},
};

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum JlrArchitecture {
    Unknown,
    Eva2,
    Eva25,
}

impl JlrArchitecture {
    pub fn new(vam: &VehicleAnnouncementMessage) -> Self {
        match vam.logical_address {
            [0x17, 0x16] => JlrArchitecture::Eva2,
            [0x17, 0x26] => JlrArchitecture::Eva25,
            _ => JlrArchitecture::Unknown,
        }
    }

    pub fn generate_ecus(&self) -> Vec<Ecu> {
        create_ecu_list()
            .into_iter()
            .filter(|ecu| ecu.architecture.contains(self)) // Keep only matching ECUs
            .collect() // Collect into a Vec<Ecu>
    }
}
