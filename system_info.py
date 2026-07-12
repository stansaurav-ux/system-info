import os
import platform
import socket
import shutil
import psutil

from datetime import datetime
now = datetime.now()
print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
username = os.getenv("USER")
cwd = os.getcwd()
os_info = platform.system()
os_release = platform.release()
python_version = platform.python_version()
hostname = socket.gethostname()
total, used, free = shutil.disk_usage("/")
memory = psutil.virtual_memory()



def main():
    print("=== System Information ===")
    # ... all your print statements here
    
if __name__ == "__main__":
    main()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

local_ip = get_local_ip()
print(f"Local IP Address: {local_ip}")
print(f"Memory Usage: {memory.used // (2**30)} GB used / {memory.total // (2**30)} GB total ({memory.percent}%)")
print(f"Disk Usage: {used // (2**30)} GB used / {total // (2**30)} GB total")
print(f"Hostname: {hostname}")
print(f"Python Version: {python_version}")
print(f"Operating System: {os_info} {os_release}")
print(f"Current Directory: {cwd}")
print(f"Username: {username}")
