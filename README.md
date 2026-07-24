🖥️ Automated Linux Server Health & Log Monitoring System
Proyek simulasi operasional Data Center yang berfokus pada pembangunan infrastruktur server virtual, konfigurasi jaringan, manajemen web server, dan otomatisasi pemantauan kesehatan sistem.

🎯 Objektif Proyek
- Membangun dan mengonfigurasi environment server bare-metal (CLI) menggunakan Ubuntu Server.
- Mengimplementasikan dasar jaringan (Static IP, DNS, routing) dan web server menggunakan Nginx.
- Membuat script otomatisasi untuk Daily Health Check sistem.
- Menganalisis dan memantau system logs untuk keperluan troubleshooting.

🛠️ Teknologi & Tools
- Virtualization: Oracle VirtualBox
- OS: Ubuntu Server 24.04 LTS (CLI only)
- Web Server: Nginx
- Scripting: Python 3 (Modul bawaan: os, shutil, subprocess)
- Linux Commands: systemctl, apt, ip, ping, tail, nano

📝 Dokumentasi Operasional (SOP)
1. Konfigurasi Server & Jaringan Dasar
   - Alokasi VM: 2 CPU, 2GB RAM, 20GB Storage (UEFI Enabled).
   - Instalasi paket dasar dan OpenSSH Server untuk akses remote.
   - Verifikasi antarmuka jaringan dan uji konektivitas keluar (ping).

2. Konfigurasi Web Server (Nginx)
   - Instalasi Nginx melalui package manager (apt).
   - Verifikasi status layanan berjalan (systemctl status nginx).
   - Uji respon HTTP internal menggunakan curl localhost.

3. Pemantauan Kesehatan Sistem (Daily Check)
   - Skrip Python (health_check.py) dikembangkan untuk memantau metrik kritikal server:
   - Kapasitas sisa Disk Space (/).
   - Beban CPU (Load Average).
   - Status berjalannya service Nginx.
<img width="1290" height="976" alt="Screenshot 2026-07-24 191557" src="https://github.com/user-attachments/assets/7f561056-1741-44ef-8d12-6573139b4a2a" />

4. Manajemen Log Sistem
   - Pemantauan lalu lintas dan error pada web server dilakukan dengan menganalisis log Nginx:
   - Access Log: tail -n 10 /var/log/nginx/access.log (Untuk melacak jejak request pengunjung).
   - Real-time Monitoring: tail -f /var/log/nginx/access.log (Untuk pemantauan insiden secara live).
