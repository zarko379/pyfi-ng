#!/usr/bin/python3
import os
import subprocess
import psutil

red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"

os.system("clear")
def root():
	return os.getuid() == 0

if root():
	pass
else:
	print(red, bold, "[+] Error: Please execute as root.")
	exit()

def interface():
	os.system("clear")
	iface_list = []
	ifaces = psutil.net_if_addrs()
	print(blue, bold, "[+] Available Interfaces:", reset)
	number = 0
	for iface, addrs in ifaces.items():
		iface_list.append(iface)
		print(green, bold, f'	[{number}] {iface}', reset)
		number += 1
	number -= 1
	iface_num = int(input(f"Select an interface [0-{number}]: "))
	if 0 <= iface_num < len(iface_list):
		selected_iface = iface_list[iface_num]
		iface = selected_iface
	else:
		print(red, bold, "[+] Please enter a valid number", reset)
		return None
	print(blue, bold, f"[+] Interface: {iface} selected", reset)

try:
	interface()
except KeyboardInterrupt:
	print(red, bold, "\n[+] Exiting...", reset)
