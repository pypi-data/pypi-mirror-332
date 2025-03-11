#[derive(Clone, Debug)]
pub struct Did {
    pub name: String,
    pub did: [u8; 2],
}

pub fn create_did_list() -> Vec<Did> {
    let list: Vec<Did> = vec![
        // Did {
        //     did: [0xf1, 0x90],
        //     name: "Vehicle Identification Number (VIN)".to_string(),
        // },
        Did {
            did: [0xf1, 0x88],
            name: "Vehicle Manufacturer ECU Software Number".to_string(),
        },
        // Did {
        //     did: [0xf1, 0x8c],
        //     name: "ECU Serial Number".to_string(),
        // },
        Did {
            did: [0xf1, 0x24],
            name: "ECU Calibration Data Number #1".to_string(),
        },
        // Did {
        //     did: [0xf1, 0x25],
        //     name: "ECU Calibration Data Number #2".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x26],
        //     name: "ECU Calibration Data Number #3".to_string(),
        // },
        Did {
            did: [0xf1, 0x11],
            name: "ECU Core Assembly Number #1".to_string(),
        },
        // Did {
        //     did: [0xf1, 0x12],
        //     name: "ECU Core Assembly Number #2".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x13],
        //     name: "ECU Delivery Assembly Number".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x08],
        //     name: "CAN Network Signal Calibration Number".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x20],
        //     name: "ECU Software Number #2".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x80],
        //     name: "Boot Software Identification Number".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x03],
        //     name: "Active Network Configuration Number".to_string(),
        // },
        // Did {
        //     did: [0xdd, 0x00],
        //     name: "Global Real Time".to_string(),
        // },
        // Did {
        //     did: [0xdd, 0x01],
        //     name: "Total Distance".to_string(),
        // },
        // Did {
        //     did: [0xf1, 0x70],
        //     name: "ECU Network Release".to_string(),
        // },
        // Did {
        //     did: [0x01, 0x02],
        //     name: "OBD MIL".to_string(),
        // },
        // Did {
        //     did: [0xee, 0x60],
        //     name: "DIM Magnitude DC Diagnostics".to_string(),
        // },
        // Did {
        //     did: [0x80, 0xd1],
        //     name: "Historical Events Data".to_string(),
        // },
    ];

    list
}
