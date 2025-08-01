from netmiko import ConnectHandler
import getpass

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
#command_script = input("Command: ")
command_list = [
	'int lo0',
	'ip address 10.10.10.1 255.255.255.255',
]
r1 = {
	"device_type" : "cisco_ios",
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
}

conn = ConnectHandler(**r1)

print(conn.send_config_set(command_list))
print(conn.send_command("show ip int br"))
conn.disconnect()