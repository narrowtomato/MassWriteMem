import netmiko
import getpass

#open files
ipsfile = open("ipsfile.txt")

#Get the username and password
username = input("user: ")
passwd = getpass.getpass("pass: ")

for ip in ipsfile:
    try:
        #Connect to the switch
        device = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=passwd)

        #Write message stating successful connection
        print("Connected successfully to " + ip )

        #Get running configuration
        writemem = device.send_command("write memory")

        #Disconnect from the switch
        device.disconnect()

        #Print command output
        print(writemem)

    except:
        #Note if the connection was unsuccessful
        print("Failed to connect to " + ip)

ipsfile.close()
