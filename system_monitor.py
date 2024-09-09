

import psutil
import time

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

def get_memory_usage():
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    print(f"Memory Usage: {memory_percent}%")

def get_disk_usage():
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    print(f"Disk Usage: {disk_percent}%")

def monitor_system():
    while True:
        print("\n----- System Monitoring -----")
        get_cpu_usage()
        get_memory_usage()
        get_disk_usage()
        time.sleep(5)  # Wait for 5 seconds before refreshing the data

if __name__ == "__main__":
    monitor_system()
