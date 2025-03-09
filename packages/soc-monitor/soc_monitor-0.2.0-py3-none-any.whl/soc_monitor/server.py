# system_monitor_v2/server.py
import asyncio
import json
import logging
import threading
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from .utils import (
    get_cpu_usage,
    get_cpu_core_usage,
    get_memory_usage,
    get_disk_usage,
    get_network_speed,
    get_top_cpu_processes,
    get_top_memory_processes,
    get_top_network_processes,
    get_wifi_details,
    get_process,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Enable CORS for frontend
origins = ["http://localhost:3000", "https://soc-tool.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ Background Updates for Fast Metrics ------------------
network_data = {"download_speed": 0, "upload_speed": 0, "ping": None}
def update_network_speed():
    global network_data
    while True:
        try:
            network_data = get_network_speed()
        except Exception as e:
            logging.error(f"Error in network monitoring: {e}")
        time.sleep(10)

threading.Thread(target=update_network_speed, daemon=True).start()

# ------------------ Heavy Metrics (Top Processes) ------------------
global_top_cpu_processes = []
global_top_memory_processes = []
global_top_network_processes = []

def update_top_processes():
    global global_top_cpu_processes, global_top_memory_processes, global_top_network_processes
    while True:
        global_top_cpu_processes = get_top_cpu_processes()
        global_top_memory_processes = get_top_memory_processes()
        global_top_network_processes = get_top_network_processes()
        time.sleep(5)

threading.Thread(target=update_top_processes, daemon=True).start()

# ------------------ WiFi Details Feature ------------------
global_wifi_details = {"SSID": None, "Signal Strength": None}
def update_wifi_details():
    global global_wifi_details
    while True:
        global_wifi_details = get_wifi_details()
        time.sleep(5)

threading.Thread(target=update_wifi_details, daemon=True).start()

# ------------------ Process Details Feature ------------------
global_process_details = None
def update_process_details():
    global global_process_details
    while True:
        global_process_details = get_process()
        time.sleep(0.05)  # Update every 50 milliseconds

threading.Thread(target=update_process_details, daemon=True).start()

# ------------------ Streaming Endpoint ------------------
async def stream_metrics():
    while True:
        data = {
            "cpu_usage": get_cpu_usage(),
            "per_core_usage": get_cpu_core_usage(),
            "memory_usage": get_memory_usage(),
            "disk_usage": get_disk_usage(),
            "network_speed": network_data,
            "wifi_details": global_wifi_details,
            "top_cpu_processes": global_top_cpu_processes,
            "top_memory_processes": global_top_memory_processes,
            "top_network_processes": global_top_network_processes,
            "process_details": global_process_details  # Process details updated every 50ms
        }
        yield f"data: {json.dumps(data)}\n\n"
        await asyncio.sleep(1)

@app.get("/metrics")
def metrics():
    return StreamingResponse(stream_metrics(), media_type="text/event-stream")

@app.get("/process")
def process():
    try:
        process_data = json.loads(global_process_details)
    except Exception as e:
        process_data = {"error": global_process_details}
    return process_data