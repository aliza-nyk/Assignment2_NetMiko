#Script that displays all the interfaces that are currently up
#Adding logging

from netmiko import ConnectHandler
from getpass import getpass

#Import Exceptions
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException


#Logging section
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#Main script
#Added Excepctions

from netmiko import ConnectHandler
from getpass import getpass
import logging

# Logging section
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Main script w/ exception handling
try:
    R1 = {
        "ip": "192.168.1.11",
        "username": "aliza",
        "password": getpass(),
        "device_type": "cisco_ios"
    }

    net_connect = ConnectHandler(**R1)


    output = net_connect.send_command("show ip int brief", use_textfsm=True)
    for i in output:
        status = i['status']
        interface = i['interface']
        IPV4 = i['ip_address']

        if status == 'up':
            print('Interface {} with IP address {} is {}'.format(interface, IPV4, status))
            print()

except ConnectionError as ce:
    logger.error('ConnectionError: ' + str(ce))
except NetMikoAuthenticationException as ae:
    logger.error('NetMikoAuthenticationException: ' + str(ae))
except NetMikoTimeoutException as nte:
    logger.error('NetMikoTimeoutException: ' + str(nte))
except Exception as e:
    logger.error('Unhandled Exception: ' + str(e))

net_connect.disconnect()
