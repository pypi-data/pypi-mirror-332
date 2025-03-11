use core::str;
use flate2::read::GzDecoder;
use reqwest::header::HeaderMap;
use std::io::{self, Cursor};
use std::path::PathBuf;
use std::{env, fs};
use tar::Archive;

/// Function to update the current executable
pub async fn update_self(version: &str) -> Result<(), Box<dyn std::error::Error>> {
    use std::process::Command;

    // Get the current executable path.
    let current_exe = env::current_exe()?;
    let temp_exe = current_exe.with_extension("new");
    let old_exe = current_exe.with_extension("old");

    let url = format!(
      "https://git-gdd.sdo.jlrmotor.com/api/v4/projects/17080/packages/generic/rapid_snapshot_tool/{}/package.tar.gz",
      version
  );

    let private_token = "gnBrohKk6cuQkF65q-c2";

    // Set up headers for the request.
    let mut headers = HeaderMap::new();
    headers.insert("PRIVATE-TOKEN", private_token.parse()?);

    // Create the HTTP client.
    let client = reqwest::Client::new();

    println!("Downloading Release...");
    let response = client.get(&url).headers(headers).send().await?;

    if !response.status().is_success() {
        eprintln!("Failed to download package: {}", response.status());
        return Err(Box::new(io::Error::new(
            io::ErrorKind::Other,
            "Failed to download package",
        )));
    }

    let content = response.bytes().await?;
    let cursor = Cursor::new(content);

    println!("Extracting package...");
    let decoder = GzDecoder::new(cursor);
    let mut archive = Archive::new(decoder);

    // Extract the files in the current directory.
    let extraction_path = PathBuf::from("./rst_temp");
    archive.unpack(&extraction_path)?;

    let extracted_exe_path = match os_info::get().os_type() {
        os_info::Type::Windows => {
            extraction_path.join("x86_64-pc-windows-gnu/release/rapid_snapshot.exe")
        }
        _ => extraction_path.join("x86_64-unknown-linux-gnu/release/rapid_snapshot"),
    };

    // Ensure the extracted executable exists.
    if !extracted_exe_path.exists() {
        eprintln!(
            "Extracted executable not found at: {:?}",
            extracted_exe_path
        );
        return Err(Box::new(io::Error::new(
            io::ErrorKind::NotFound,
            "Extracted executable not found",
        )));
    }

    println!("Replacing current executable...");
    if cfg!(target_os = "windows") {
        // On Windows, rename the current executable to `.old`.
        fs::rename(&current_exe, &old_exe)?;

        // Move the new executable to the original path.
        fs::rename(&extracted_exe_path, &current_exe)?;

        let _ = std::fs::remove_file(&old_exe);
        let _ = std::fs::remove_dir_all(&extraction_path);

        println!("Update complete. Restarting application...");

        let new_version = Command::new(current_exe).arg("-V").output()?.stdout;
        let new_version_ascii = match str::from_utf8(&new_version) {
            Ok(v) => v.trim(),
            Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
        };

        println!("Updated to: {:?}", new_version_ascii);

        std::process::exit(0); // Exit the current process to allow the restart.
    } else {
        // On Unix-like systems, move the new executable into place directly.
        fs::rename(&extracted_exe_path, &temp_exe)?;
        fs::rename(&temp_exe, &current_exe)?;

        let _ = std::fs::remove_file(&old_exe);
        let _ = std::fs::remove_dir_all(&extraction_path);

        println!("Update complete. Restarting application...");
        Command::new(current_exe).arg("-V").spawn()?;
        std::process::exit(0);
    }
}
