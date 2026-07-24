import shutil
import os
import subprocess

print("=== Laporan Kesehatan Server ===")

# 1. Cek Kapasitas Disk
disk = shutil.disk_usage("/")
free_disk = disk.free / (1024 ** 3)
print(f"Sisa Disk   : {free_disk:.2f} GB")

# 2. Cek Beban CPU
cpu_load = os.getloadavg()
print(f"Beban CPU   : {cpu_load[0]} (dalam 1 menit terakhir)")

# 3. Cek Status Nginx
try:
    status = subprocess.check_output(["systemctl", "is-active", "nginx"], text=True).strip()
    print(f"Status Nginx: {status}")
except Exception:
    print("Status Nginx: bermasalah")
