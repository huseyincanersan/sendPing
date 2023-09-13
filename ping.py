import os
import platform
import subprocess
import threading
import time
from ping3 import ping, verbose_ping

with open("ipAddresses", "r") as  file:
    ipAddresses = file.read().split("\n")
    ipAddresses = [item for item in ipAddresses if item != ""]


def send_ping(ip):
    try:

        response = ping(ip)
        if (response is not None) and (response != False) :
            online.append(f"{ip} yanit verdi. Ping suresi: {response} ms\n" )

        else:
            offline.append(f"{ip} yanit vermedi.\n")



    except Exception as e:
        error.append(e)
        

threads = []
online  = []
offline = []
error   = []
for ip in ipAddresses:
    thread = threading.Thread(target=send_ping, args=(ip,))
    threads.append(thread)
    thread.start()



for thread in threads:
    thread.join()

with open("online.txt","w") as file:
    for x in online:
        file.write(x+ "\n")

with open("offline.txt","w") as file:
    for y in offline:
        file.write(y+ "\n")
