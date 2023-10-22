#!/usr/bin/python3
import pyfiglet
import os

red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"

def main():
	custom_fig = pyfiglet.Figlet(font='doom')
	ascii_art = custom_fig.renderText('Pyfi-ng')
	os.system("clear")
	print(blue, bold, "-----------------------------------\n", ascii_art, "\n Made by Zarko", "\n------------------------------------", reset)
	print(blue, bold, "\n\nTools: ", reset)
	print("		[0] Scan Wifi Networks")
	print("		[1] Get Handshake cap file")
	print("		[2] Wi-Fi Deauth Attack")
	print("		[3] Wi-Fi DDoS")
	print("		[4] Brute Force Password from dictionary")
	print("		[5] Security analysis (show if networks require a password)")
	print("		[6] Beacon Flood Attack")
	script = input("\nWhat do you want to do? [0-6]: ")

if __name__ == "__main__":
	main()
