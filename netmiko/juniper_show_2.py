#### show version with JSON parsing data output

from netmiko import ConnectHandler
import getpass
import json

ip_router = input("IP router: ")
user_login = input("Username: ")
pass_login = getpass.getpass()
r1 = {
	"device_type" : "juniper_junos",
	"ip" : ip_router,
	"username" : user_login,
	"password" : pass_login,
	"port" : 2224,
}

with ConnectHandler(**r1) as conn:
    print("[*] Connected to Juniper")
    output = conn.send_command("show version | display json", use_textfsm=False)
    
    try:
        data = json.loads(output)
        version_info = data['software-information'][0]
        #host_name = version_info.get("host-name", "N/A")
        host_name = version_info['host-name'][0]['data']
        junos_version = version_info['junos-version'][0]['data']
        model = version_info['product-name'][0]['data']
        print(f"Hostname: {host_name}")
        print(f"Junos Version: {junos_version}")
        print(f"Model: {model}")
    except Exception as e:
        print("Parsing failed:", e)