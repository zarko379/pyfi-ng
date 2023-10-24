#!/usr/bin/python3
import importlib
import os
import sys
import time

red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"

libraries = ['pyfiglet', 'pyrcrack', 'psutil']
version = "0.01"

def root():
        return os.getuid() == 0

if root():
        pass
else:
        print(red, bold, "[+] Error: Please execute as root.")
        exit()

def check_lib(lib):
	try:
		importlib.import_module(lib)
		return True
	except ImportError:
		return False

for lib in libraries:
	if not check_lib('pyrcrack'):
		os.system("wget https://github.com/XayOn/pyrcrack/releases/download/1.2.6/pyrcrack-1.2.6-py3-none-any.whl")
		os.system("python3 -m pip install pyrcrack-1.2.6-py3-none-any.whl")
		os.system("rm pyrcrack-1.2.6-py3-none-any.whl")
	if not check_lib(lib):
		print(f"Downloading missing libraries ({lib})...")
		os.system(f"python3 -m pip install {lib}")

os.system("clear")

for lib in libraries:
	if check_lib(lib):
		exec(f'import {lib}')

def main():
	try:
		custom_fig = pyfiglet.Figlet(font='slant')
		ascii_art = custom_fig.renderText('WifSniff3')
		os.system("clear")
		print(blue, bold, "-----------------------------------\n", ascii_art, f"\n Made by Zarko | V {version}", "\n------------------------------------", reset)
		print(blue, bold, "\n\nTools: ", reset)
		print("		[0] Scan Wifi Networks")
		print("		[1] Get Handshake cap file")
		print("		[2] Wi-Fi Deauth Attack")
		print("		[3] Wi-Fi DDoS")
		print("		[4] Brute Force Password from dictionary")
		print("		[5] Security analysis (show if networks require a password)")
		print("		[6] Beacon Flood Attack")
		option = ""
		option = input("\nWhat do you want to do? [0-6]: ")
		if option.isdigit():
			script = int(option)
		else:
			print(red, bold, "[+] Please use a number", reset)
			exit()
		scripts = ["./bin/scan.py", "./bin/handshake.py", "./bin/deauth.py", "./bin/ddos.py", "./bin/brute_force.py", "./bin/sec_analysis.py", "./bin/beacon_attack.py"]

		if 0 <= script < len(scripts):
			script = scripts[script]
			launch = script
			try:
				os.system(f'sudo {launch}')
			except FileNotFoundError:
				print(red, bold, f"File {launch} was not found. Make sure you are in the root folder of the script", reset)
		elif script >= len(scripts):
			print(red, bold, "[+] Please enter a valid number", reset)
			exit()
	except KeyboardInterrupt:
		os.system("clear")
		print(red, bold, "\n[+] Exiting...", reset)

if __name__ == "__main__":
	main()
