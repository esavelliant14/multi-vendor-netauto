from netmiko import ConnectHandler
import getpass

user_login = input("Username: ")
pass_login = getpass.getpass()
command_script = input("Command: ")

r1 = {
	"device_type" : "cisco_ios",
	"ip" : "192.168.147.2",
	"username" : user_login,
	"password" : pass_login,
}

r2 = {
	"device_type" : "cisco_ios",
	"ip" : "192.168.147.2",
	"username" : user_login,
	"password" : pass_login,
}

all_router = [r1,r2]

for router in all_router:

	conn = ConnectHandler(**router)
	print("IP Address on {}".format(router["ip"]))
	print(conn.send_command(command_script))
	print("\n")

