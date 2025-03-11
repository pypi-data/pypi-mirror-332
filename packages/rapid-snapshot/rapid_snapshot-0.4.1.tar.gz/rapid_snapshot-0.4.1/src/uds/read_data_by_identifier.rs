use crate::uds::definitions::*;
use crate::uds::message::Service;

struct ReadDataByIdentifier {
    pub data_identifier: [u8; 2],
    pub data_record: Vec<u8>,
}

impl ReadDataByIdentifier {
    pub fn new() {}
}

impl Service for ReadDataByIdentifier {
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
