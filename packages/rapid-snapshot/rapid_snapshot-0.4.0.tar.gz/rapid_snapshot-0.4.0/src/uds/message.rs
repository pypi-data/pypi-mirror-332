use crate::uds::definitions::*;

struct UdsMessage {
    pub service_identifier: ServiceIdentifier,
}

impl UdsMessage {
    pub fn new(sid: ServiceIdentifier) -> Self {
        Self {
            service_identifier: sid,
        }
    }
}

impl Service for UdsMessage {
    fn to_bytes(&self) -> Vec<u8> {
        todo!()
    }

    fn from_bytes(bytes: &[u8]) -> Option<Self> {
        todo!()
    }

    fn len(&self) -> usize {
        self.to_bytes().len()
    }
}

enum ServiceIdentifier {
    ReadDataByIdentifier(Vec<u8>),
    // Error(Vec<u8>),
}

pub trait Service: Sized {
    fn to_bytes(&self) -> Vec<u8>;
    fn from_bytes(bytes: &[u8]) -> Option<Self>;
    fn len(&self) -> usize;
}

impl Service for ServiceIdentifier {
    fn to_bytes(&self) -> Vec<u8> {
        todo!()
    }

    fn from_bytes(bytes: &[u8]) -> Option<Self> {
        todo!()
    }

    fn len(&self) -> usize {
      self.to_bytes().len()
    }
}

// fn test() {
//     let uds = UdsMessage::new(ServiceIdentifier::ReadDataByIdentifier(vec![
//         0x4e, 0x43, 0x52, 0x32, 0x32, 0x51, 0x32, 0x20, 0x49, 0x47, 0x4d, 0x20, 0x20, 0x20, 0x20,
//         0x20,
//     ]));
// }
