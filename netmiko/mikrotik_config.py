from netmiko import ConnectHandler
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
#command_script = input("Command: ")
command_list = [
	'int br add name="lo0"',
	'ip address add address="10.10.10.2/32" interface=lo0',
]
r1 = {
	"device_type" : "mikrotik_routeros",
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
}

conn = ConnectHandler(**r1)

print(conn.send_config_set(command_list))
print(conn.send_command("ip address print"))
conn.disconnect()