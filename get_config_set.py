#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass


# Logs in to PanOS device and prompts for credentials
hostname = input("Enter PanoOS FQDN/IP: ")
print("This account will be used to login to Panorama, and firewalls")
user = input("Enter your service account: ")

#password = getpass.getpass("Password: ")

#return hostname, username

#command3 = input("Would you like to run any additional commands? If so enter now:")


mydevice = {
    "host":  hostname ,
    "username": user,
    "password": getpass(),
    "device_type": "paloalto_panos",
}

net_connect = Netmiko(**mydevice)
command = "set cli config-output-format set"
command1 = "set cli pager off"
command2 = "configure"
command3 = "show"
print()
print(net_connect.find_prompt())
output0 = net_connect.send_command(command)
output1 = net_connect.send_command(command1)
output2 = net_connect.config_mode(command2)
output3 = net_connect.send_command(command3)
net_connect.disconnect()
print(output3)
print()
