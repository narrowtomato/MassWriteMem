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

        #Parse out info relative to port secuirty and write to output file
        print(ip)
        print(writemem)

    except:
        #Note that the connection was unsuccessful
        print("Failed to connect to " + ip)

ipsfile.close()
