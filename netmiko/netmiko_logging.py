###aktivitas login tercatat di sebuah log

from netmiko import ConnectHandler
import logging
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
merk = input("Merk Perangkat (cisco_ios/mikrotik_routeros/juniper_junos): ")
port_ssh = input("port ssh: ")
r1 = {
	"device_type" : merk,
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
	"port" : port_ssh
}

logging.basicConfig(filename='netauto.log', level=logging.INFO)

try:
    # koneksi Netmiko
    conn = ConnectHandler(**r1)
    logging.info(f"Sukses konek ke {r1['ip']}")
    conn.disconnect()

except Exception as e:
    logging.error(f"Gagal koneksi ke {r1['ip']}: {str(e)}")