from netmiko import ConnectHandler
import getpass

ip_router = input("Masukkan IP Address (pisahkan dengan koma): ")
user_login = input("Username: ")
pass_login = getpass.getpass()
command_script = input("Command: ")

ip_list = ip_router.split(",")

for ip in ip_list:
	router = {
		"device_type" : "cisco_ios",
		"ip" : ip,
		"username" : user_login,
		"password" : pass_login,
	}


	conn = ConnectHandler(**router)
	print("IP Address on {}".format(router["ip"]))
	print(conn.send_command(command_script))
	print("\n")
