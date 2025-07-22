from netmiko import ConnectHandler
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
command_script = input("Command: ")
r1 = {
	"device_type" : "mikrotik_routeros",
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
}

conn = ConnectHandler(**r1)

print(conn.send_command(command_script))
conn.disconnect()