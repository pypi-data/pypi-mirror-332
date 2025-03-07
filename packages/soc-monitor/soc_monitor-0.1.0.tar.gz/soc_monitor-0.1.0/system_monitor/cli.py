# soc_monitor/cli.py
import subprocess
import sys
import os
import signal
from soc_monitor.server import app
import uvicorn

def start_server():
    """Start the FastAPI server."""
    print("Starting system monitor server...")
    uvicorn.run(app, host="0.0.0.0", port=8123)

def stop_server():
    """Stop the FastAPI server."""
    print("Stopping system monitor server...")
    try:
        # Find the process ID of the running server
        result = subprocess.run(["lsof", "-i", ":8123"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        if len(lines) > 1:
            pid = int(lines[1].split()[1])
            os.kill(pid, signal.SIGTERM)
            print(f"Stopped server with PID {pid}")
        else:
            print("No server running on port 8123.")
    except Exception as e:
        print(f"Error stopping server: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: soc-monitor <start|stop>")
        sys.exit(1)

    command = sys.argv[1]
    if command == "start":
        start_server()
    elif command == "stop":
        stop_server()
    else:
        print("Invalid command. Use 'start' or 'stop'.")
        sys.exit(1)

if __name__ == "__main__":
    main()