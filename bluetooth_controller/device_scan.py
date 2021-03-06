'''
bluetooth device scanner
'''
import time
import bluetooth

alreadyFound = []
def findDevs():
    foundDevs = bluetooth.discover_devices(lookup_names=True)
    for(addr,name) in foundDevs:
        if addr not in alreadyFound:
            print "[*] Found Bluetooth Device :  " +str(name)
            print "[+] MAC address :  " +str(addr)
            alreadyFound.append(addr)

while True:
    findDevs()
    time.sleep(5)