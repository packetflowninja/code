#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass


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
#command2 = input("Would you like to run any additional commands? If so enter now:")

# Device settings from user input
mydevice = {
    "host":  hostname ,
    "username": user,
    "password": getpass(),
    "device_type": "paloalto_panos",
}

net_connect = Netmiko(**mydevice)
command = "show running rule-use highlight rule-base security type unused vsys vsys1"
command2 = "show running rule-use highlight rule-base nat type unused vsys vsys1"
command3 = "show running rule-use highlight rule-base decryption type unused vsys vsys1"

print("---------------------------------------------")
print(net_connect.find_prompt())
output = net_connect.send_command(command)
output2 = net_connect.send_command(command2)
output3 = net_connect.send_command(command3)
net_connect.disconnect()
choice = input( "Would you like yout output in terminal or a file? Please enter T or F: ")
if choice == "f" or "F":
     reportfile = open ( hostname + 'UnusedRules_NATs_Decyrpt_Profiles', 'a')
     reportfile.write ("Unused Security Rules\n") + reportfile.write (output) +reportfile.write ("Unused NAT Rules\n") + reportfile.write (output2) + reportfile.write ("Unused Decrypt Polices\n") + reportfile.write (output3)
else:
    print(output)
    print(output2)
    print(output3)
