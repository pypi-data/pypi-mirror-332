#!/bin/bash

cargo build --release --target=x86_64-pc-windows-msvc
mv ./target/x86_64-pc-windows-msvc/release/rapid_snapshot.exe ./