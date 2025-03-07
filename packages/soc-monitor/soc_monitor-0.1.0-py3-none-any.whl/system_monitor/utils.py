# soc_monitor/utils.py
import psutil
from speedtest import Speedtest

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
        return {"download_speed": 0, "upload_speed": 0, "ping": None}