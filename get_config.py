#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import datetime


d=datetime.date.today()
dt=d.strftime
print(dt("%m-%w-%Y"))


# Logs in to PanOS device and prompts for credentials
hostname = input("Enter PanoOS FQDN/IP: ")
print("--------------------------------------------------------------------")
print("This account will be used to pull config from Panorama or firewall")
print("--------------------------------------------------------------------")
print()
print("--------------------------------------------------------------------")
user = input("Enter your service account: ")
print("--------------------------------------------------------------------")

# You can add additinal commands if encessary, like "show clock" for time stamp or any other PanOS command
# Commenting this line out as there is no current need for it.
# command2 = input("Would you like to run any additional commands? If so enter now:")

# Device settings from user input
mydevice = {
    "host":  hostname ,
    "username": user,
    "password": getpass(),
    "device_type": "paloalto_panos",
}
d=datetime.date.today()
net_connect = Netmiko(**mydevice)
command = "show config running"
print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
choice = input( "Would you like yout output in terminal or a file? Please enter T or F: ")
if choice == "f" or "F":
     reportfile = open (hostname+'config_backup.xml', 'a')
     reportfile.write (output)
else:
    print(output)
