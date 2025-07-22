from netmiko import ConnectHandler
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
#command_script = input("Command: ")
command_list = [
	'set interfaces lo0 unit 0 family inet address 10.10.10.3/32',
]
r1 = {
	"device_type" : "juniper",
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
}

conn = ConnectHandler(**r1)

print(conn.send_config_set(command_list))
print(conn.commit())
print(conn.send_command("run show interface terse"))
conn.disconnect()