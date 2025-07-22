from netmiko import ConnectHandler
import getpass

user_login = input("Username: ")
pass_login = getpass.getpass()
command_script = input("Command: ")

for x in range(2,3):
	router = {
		"device_type" : "cisco_ios",
		"ip" : "192.168.147.{}".format(x),
		"username" : user_login,
		"password" : pass_login,
	}


	conn = ConnectHandler(**router)
	print("IP Address on {}".format(router["ip"]))
	print(conn.send_command(command_script))
	print("\n")

### 2,3 artinya 2 saja, kalau 1,3 berarti 1 dan 2, itu x nya untuk oktet terakhir di ip address,

### tambahan, kalau 1,10 berarti segmen ip yang terpakai 192.168.147.1-192.168.147.9