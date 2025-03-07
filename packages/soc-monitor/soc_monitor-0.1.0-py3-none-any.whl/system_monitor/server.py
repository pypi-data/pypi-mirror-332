# soc_monitor/server.py
import os
import psutil
from speedtest import Speedtest
import asyncio
import time
import threading
import json
import logging
import subprocess
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

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

# ------------------ Fast Metrics ------------------
def get_cpu_usage():
    return psutil.cpu_percent(interval=0)

def get_cpu_core_usage():
    return psutil.cpu_percent(interval=0, percpu=True)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    total, used, free = 0, 0, 0
    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
            total += usage.total
            used += usage.used
            free += usage.free
        except PermissionError:
            continue
    return round((used / total) * 100, 2) if total else 0

def get_network_speed():
    try:
        st = Speedtest()
        st.get_best_server()
        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        ping = round(st.results.ping, 2)
        return {"download_speed": download, "upload_speed": upload, "ping": ping}
    except Exception as e:
        logging.warning(f"Network error: {e}")
        return {"download_speed": 0, "upload_speed": 0, "ping": None}

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
def get_top_cpu_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu_percent": proc.info['cpu_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)[:5]

def get_top_memory_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "memory_percent": round(proc.info['memory_percent'], 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return sorted(processes, key=lambda x: x["memory_percent"], reverse=True)[:5]

def get_top_network_processes():
    process_data = []
    for proc in psutil.process_iter(['name']):
        try:
            connections = proc.connections()
            if connections:
                process_data.append({
                    "name": proc.info['name'],
                    "connections": len(connections)
                })
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    process_data.sort(key=lambda x: x["connections"], reverse=True)
    return process_data[:5]

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
def get_wifi_details():
    try:
        result = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        ssid = None
        signal = None
        for line in result.splitlines():
            if "SSID" in line and "BSSID" not in line:
                parts = line.split(":", 1)
                if len(parts) == 2:
                    ssid = parts[1].strip()
            if "Signal" in line:
                parts = line.split(":", 1)
                if len(parts) == 2:
                    signal = parts[1].strip()
        if ssid and signal:
            return {"SSID": ssid, "Signal Strength": signal}
        else:
            return {"SSID": None, "Signal Strength": None}
    except Exception as e:
        logging.warning("WiFi details error: " + str(e))
        return {"SSID": None, "Signal Strength": None}

global_wifi_details = {"SSID": None, "Signal Strength": None}
def update_wifi_details():
    global global_wifi_details
    while True:
        global_wifi_details = get_wifi_details()
        time.sleep(5)

threading.Thread(target=update_wifi_details, daemon=True).start()

# ------------------ New: Process Details Feature ------------------
def get_process():
    result = subprocess.run(
        ["powershell", "-command", "Get-Process | Select-Object Id, SI, ProcessName, CPU, Handles, NPM, PM, WS | ConvertTo-Json -Depth 10"],
        capture_output=True,
        text=True
    )
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"

# Update process details every 50 milliseconds
global_process_details = None
def update_process_details():
    global global_process_details
    while True:
        global_process_details = get_process()
        time.sleep(0.05)  # 50 milliseconds

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
            "process_details": global_process_details  # integrated process info updated every 50ms
        }
        yield f"data: {json.dumps(data)}\n\n"
        await asyncio.sleep(1)

@app.get("/metrics")
def metrics():
    return StreamingResponse(stream_metrics(), media_type="text/event-stream")

# ------------------ New: Process Endpoint ------------------
@app.get("/process")
def process():
    try:
        process_data = json.loads(global_process_details)
    except Exception as e:
        process_data = {"error": global_process_details}
    return process_data