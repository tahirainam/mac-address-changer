import subprocess

interface = input("interface: ") #use eth0 for wired or virtual adapter and wlan0 for wireless
new_mac = input("new MAC address: ")

print("[+] changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True) 
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True) 
subprocess.call("ifconfig " + interface + " up", shell=True) 