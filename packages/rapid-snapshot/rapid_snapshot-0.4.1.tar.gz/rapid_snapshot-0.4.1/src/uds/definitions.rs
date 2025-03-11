// Service Identifiers
pub const DIAGNOSTIC_SESSION_CONTROL: u8 = 0x10;
pub const ECU_RESET: u8 = 0x11;
pub const SECURITY_ACCESS: u8 = 0x27;
pub const COMMUNICATION_CONTROL: u8 = 0x28;
pub const TESTER_PRESENT: u8 = 0x3e;
pub const AUTHENTICATION: u8 = 0x29;
pub const SECURED_DATA_TRANSMISSION: u8 = 0x84;
pub const CONTROL_DTC_SETTING: u8 = 0x85;
pub const RESPONSE_ON_EVENT: u8 = 0x86;
pub const LINK_CONTROL: u8 = 0x87;
pub const READ_DATA_BY_IDENTIFIER: u8 = 0x22;
pub const READ_MEMORY_BY_ADDRESS: u8 = 0x23;
pub const READ_SCALING_DATA_BY_IDENTIFIER: u8 = 0x24;
pub const READ_DATA_BY_PERIODIC_IDENTIFIER: u8 = 0x2a;
pub const DYNAMICALLY_DEFINE_DATA_IDENTIFIER: u8 = 0x2c;
pub const WRITE_DATA_BY_IDENTIFIER: u8 = 0x2e;
pub const WRITE_MEMORY_BY_ADDRESS: u8 = 0x3d;
pub const CLEAR_DIAGNOSTIC_INFORMATION: u8 = 0x14;
pub const READ_DTC_INFORMATION: u8 = 0x19;
pub const INPUT_OUTPUT_CONTROL_BY_IDENTIFIER: u8 = 0x2f;
pub const ROUTINE_CONTROL: u8 = 0x31;
pub const REQUEST_DOWNLOAD: u8 = 0x34;
pub const REQUEST_UPLOAD: u8 = 0x35;
pub const TRANSFER_DATA: u8 = 0x36;
pub const REQUEST_TRANSFER_EXIT: u8 = 0x37;
pub const REQUEST_FILE_TRANSFER: u8 = 0x38;
pub const ERROR: u8 = 0x3f;

// Read Data By Identifier (RDBI)
// General
pub const RDBI_MIN_LENGTH: usize = 3;

// RDBI Positive Response Codes
pub const RDBI_POSITIVE_RES: u8 = 0x62;

// Negative Response Codes
pub const RDBI_INCORRECT_MESSAGE_LENGTH_OR_INVALID_FORMAT: u8 = 0x13;
pub const RDBI_RESPONSE_TOO_LONG: u8 = 0x14;
pub const RDBI_CONDITIONS_NOT_CORRECT: u8 = 0x22;
pub const RDBI_REQUEST_OUT_OF_RANGE: u8 = 0x31;
pub const RDBI_SECURITY_ACCESS_DENIED: u8 = 0x33;
