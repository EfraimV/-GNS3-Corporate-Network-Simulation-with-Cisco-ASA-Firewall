import os
import subprocess

ip_list = [
    "192.168.10.1",
    "192.168.10.2",
    "10.2.2.1",
    "192.168.50.1"
]

for ip in ip_list:
    print(f"Pinging {ip}...", end=' ')
    result = subprocess.run(["ping", "-c", "2", ip], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print("✅ Reachable")
    else:
        print("❌ Unreachable")
