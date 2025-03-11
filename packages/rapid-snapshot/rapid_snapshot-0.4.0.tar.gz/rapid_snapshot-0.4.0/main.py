import asyncio
from rapid_snapshot import PySnapshotArgs, LogLevel, snapshot_vehicle_sync


async def main():
    args = PySnapshotArgs(
        custom_path=None,  # No custom path provided
        log_level=LogLevel.Trace,  # Set logging level to Info
        delay=5,  # 5-second delay
    )

    try:
        await snapshot_vehicle_sync(args)  # Call the Rust function asynchronously
        print("Snapshot completed successfully!")
    except Exception as e:
        print(f"Error during snapshot: {e}")


# Run the async function
asyncio.run(main())
