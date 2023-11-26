'''
	Created by Lewis Kamau Kimaru
	function: Automatically switches between DHCP - Static IP configurations
'''
import subprocess  # open .bat files
import socket  # get IP
import smtplib
import os
import sys
import time


# get network adapter name
def adapter():
    response = os.popen('netsh interface show interface | find "Connected"').read()
    response = list(response.replace('\n', '').split())

    if 'Connected' in response:
        return response[-1]


name = adapter()


# 1 Edit & run DHCP.bat file
def dhcp(name):
    dhcp = open(r"C:\Netcon\Connected\DHCP.bat", "w").write(
        f"@echo off\nnetsh interface ipv4 set address name=\"{name}\" source=dhcp\n@echo off\nnetsh interface ipv4 set dns name=\"{name}\" source=dhcp")

    return dhcp


dhcp(name)

# run DHCP.bat
subprocess.call([r"C:\Netcon\Connected\DHCP.bat"])

# delay to register dhcp
time.sleep(1)
print("DHCP set")

# 2 Get IPv4 address
# Get IP Address
while True:
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    if IPAddr == "127.0.0.1" or IPAddr == "169.254.0.1":
        sys.exit("Not connected to the Network")
    else:
        print(hostname)
        break
# get IPv4 Address
subprocess.call([r"C:\Netcon\Get IPv4\get IPv4.bat"])
time.sleep(1)
while True:
    ipv4 = []
    with open(r"C:\Netcon\Get IPv4\IPv4.txt") as f:
        for line in f:
            for word in line.split():
                ipv4.append(word)
    ip = ipv4[0]  # ip address
    netmask = ipv4[1]  # subnet mask
    dgw = ipv4[2]  # Default Gateway
    print(f'ip = {ip}\nnetmask = {netmask}\ndgw = {dgw}')
    break


# 3 Send IPv4 Email
def sendIP(hostname, IPAddr, name):
    time.sleep(0.5)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("sender@gmail.com", "#################")
    server.sendmail("sender@gmail.com",
                    "receiver@gmail.com",
                    f"\nComp ID: ( {hostname} )\nNew IP: ( {IPAddr} )\nCurrent Adapter: ( {name} )")

    server.quit()
    print("\nEmail sent\n")


sendIP(hostname, IPAddr, name)


# 4 add IPv4 to static.bat
def IPv4(name, ip, netmask, dgw):
    static = open(r"C:\Netcon\Connected\new-static.bat", "w").write(
        "@echo off \nnetsh interface ipv4 set address name=\"" + name + f"\" static {ip} {netmask} {dgw} ")

    print("Static IP saved")
    return static


IPv4(name, ip, netmask, dgw)

# 5 run static.bat
subprocess.call([r"C:\Netcon\Connected\new-static.bat"])
print("Static IP set\n")

# 6 Close cmd
time.sleep(1)
print("Closing CMD\n \ncopyright ©kimaru 2023")
os.system("taskkill /im cmd.exe /f")
# end
