from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
from datetime import datetime
import os
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
merk = input("Merk Perangkat (cisco_ios/mikrotik_routeros/juniper_junos): ")
port_ssh = input("port ssh: ")

# Informasi perangkat (contoh: Cisco IOS)
device = {
    "device_type": merk,
    "ip": ip_router,
    "username": user_login,
    "password": pass_login,
}

# Daftar command backup
if device["device_type"] == "cisco_ios":
    backup_commands = [
        "show running-config",
        "show version"
    ]
elif device["device_type"] == "juniper_junos":
    backup_commands = [
        "show configuration | no-more",
        "show version"
    ]
elif device["device_type"] == "mikrotik_routeros":
    backup_commands = [
        "export",
    ]
# Persiapan nama file backup
timestamp = datetime.now().strftime("%Y%m%d-%H%M")
hostname = device.get("ip", "unknown")
vendor = device.get("device_type", "device")
filename = f"{vendor}-{hostname}_{timestamp}.txt"

# Folder penyimpanan
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)
filepath = os.path.join(backup_dir, filename)

print(f"[INFO] Mulai backup ke {hostname}...\n")

try:
    conn = ConnectHandler(**device)

    with open(filepath, "w", encoding="utf-8") as f:
        for cmd in backup_commands:
            print(f"[INFO] Menjalankan: {cmd}")
            output = conn.send_command(cmd)
            f.write(f"\n{'='*40}\nCommand: {cmd}\n{'='*40}\n")
            f.write(output)
            f.write("\n\n")

    conn.disconnect()
    print(f"\n[SUCCESS] Backup selesai dan disimpan di: {filepath}")

except NetmikoAuthenticationException:
    print(f"[ERROR] Login gagal ke {hostname}")
except NetmikoTimeoutException:
    print(f"[ERROR] Timeout ke {hostname}")
except Exception as e:
    print(f"[ERROR] {hostname}: {e}")
