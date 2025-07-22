from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
merk = input("Merk Perangkat (cisco_ios/mikrotik_routeros/juniper_junos): ")
port_ssh = input("port ssh: ")
command_script = input("Command: ")
r1 = {
	"device_type" : merk,
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
	"port" : port_ssh
}

try:
    conn = ConnectHandler(**r1)
    output = conn.send_command(command_script)
    print(output)
    conn.disconnect()
except NetMikoAuthenticationException:
    print(f"[ERROR] Auth gagal untuk {r1['ip']}")
except NetMikoTimeoutException:
    print(f"[ERROR] Timeout, tidak bisa konek ke {r1['ip']}")
except Exception as e:
    print(f"[ERROR] Umum: {e}")