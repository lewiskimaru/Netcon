'''
	Created by Lewis Kamau Kimaru
	Checks if the device is connected to the desired WIFI network
'''

import os
import platform
import subprocess

while True:
    if platform.system() == "Windows":
        response = os.popen(f"netsh wlan connect name=ITS.").read() # change ITS to your WIFI SSID
        if "failed" in response:
            response = os.popen("netsh wlan connect name=FIDS_T2").read() # Change FIDS_T2 to your WIFI SSID
            if "failed" in response:
                os.system("taskkill /im cmd.exe /f")
            else:
                subprocess.call([r"C:\Netcon\Connected\run_setuping.bat"])
                os.system("taskkill /im cmd.exe /f")
        else:
            subprocess.call([r"C:\Netcon\Connected\run_setuping.bat"])
            os.system("taskkill /im cmd.exe /f")
    break
    
print("copyright ©kimaru 2023")

