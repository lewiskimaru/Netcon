'''
	Created by Lewis Kamau Kimaru
	function: Checks if the system is Configured correctly (troubleshoots)
'''

import os
import time
import subprocess

#  delay
time.sleep(2)

# KAA Ping test
KAA = ['10.15.7.13']  # Change IP to a stable IP in your network
for kip in KAA:
    response = os.popen(f"ping {kip}").read()
    if "bytes=32" in response:
        kping = 1  # ping Successful
        print(f"{kping}\n")
    else:
        kping = 0  # ping Unsuccessful
        print(f"{kping}\n")

# Google ping test
while True:
    response = os.popen(f"ping google.com").read()
    if "bytes=32" in response:
        gping = 1  # ping successful
        print(gping)
    else:
        gping = 0  # ping Unsuccessful
        print(gping)
    break

# Establish connection
if kping == 1 and gping == 0:
    print("Secure connection")
    os.system("taskkill /im cmd.exe /f")

else:
    print("No \ Unsecure connection")
    # run dhcp to static ip script
    subprocess.call([r"C:\Netcon\Connected\Run_Script.bat"])

print("copyright ©kimaru 2023")
