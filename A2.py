#Import modules

from netmiko import ConnectHandler
from getpass import getpass

#Define device params
R1 = {
    "ip":"192.168.1.11",
    "username":"aliza",
    "password":getpass(),
    "device_type":"cisco_ios"
}

#Make connection session with target device
net_connect = ConnectHandler(**R1)

#Body of program
config = ["router ospf 1","network 192.168.1.0 0.0.0.255 area 0"]
output = net_connect.send_config_set(config)
output += net_connect.save_config()
output += net_connect.send_command("show ip ospf database")

print()
print(output)
print()

#Disconnect
net_connect.disconnect()
