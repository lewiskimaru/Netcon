'''
	Created by Lewis Kamau Kimaru
	function: Checks connection status i.e if device is online or offline
'''
import subprocess
import os
import sys
import time


def checkConnection():
    time.sleep(1)  # wait for win auto
    result = os.popen(f"arp -a").read()
    if "No ARP Entries Found." in result:
        print("Offline")
        # subprocess.call([r"C:\Netcon\Disconnected\con-net.bat"])
        sys.exit("No connection")  # on ethernet
    else:
        command = r"powershell Get-NetConnectionProfile | select 'Name'"
        data = str(subprocess.check_output(command))
        if "Unidentified network" in data:
            print("Unidentified network")
            subprocess.call([r"C:\Netcon\Connected\Run_Script.bat"])
        else:
            print("Online\n \nChopped by Lewis")
            subprocess.call([r"C:\Netcon\Connected\run_setuping.bat"])


checkConnection()
print("copyright ©kimaru 2023")

