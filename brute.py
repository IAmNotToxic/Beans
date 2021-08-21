import os, sys, time, colorama
from time import sleep as timeout
from colorama import Fore
def restart_program():
	os.system(' clear ')	
print(Fore.BLUE+"██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗ ")
time.sleep(0.1)
print(Fore.BLUE+"██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝ ")
time.sleep(0.1)
print(Fore.BLUE+"██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗   ")
time.sleep(0.1)
print(Fore.BLUE+"██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝   ")
time.sleep(0.1)
print(Fore.BLUE+"██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗ ")
time.sleep(0.1)
print(Fore.BLUE+"╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ ")
time.sleep(0.1)                                                                                       
print
print(Fore.RED+" A ighack:     ")
time.sleep(0.1)
print(Fore.BLUE+" B instahack: ")
time.sleep(0.1)
print(Fore.RED+" C instabrute: ")
time.sleep(0.1)
print(Fore.BLUE+" D FB Brute:  ")
time.sleep(0.1)
print(Fore.RED+" E Install:    ")
time.sleep(0.1)
print(Fore.BLUE+" 0 Exit:	   ")
time.sleep(0.1)
print
brute = input(" Brute Force ==>> ")

if brute == 'A' or 'a':
	os.system(' clear ')
	os.system(' pip3 install lolcat && cd ighack && bash setup && bash ighack.sh')

if brute == 'B' or 'b':
	os.system(' clear ')
	os.system(' cd instahack && bash setup && bash instahack.sh ')

if brute == 'C' or 'c':
	os.system(' clear ')
	os.system(' cd igbrute && bash setup && bash igbrute.sh ')	

if brute == 'D' or 'd':
	os.system(' clear ')
	os.system(' pip3 install mechanize && pip3 install requests bs4 && cd Facebook-BruteForce && python3 fb.py ')

if brute == 'E' or 'e':
	os.system(' clear ')
	print(" Wait 5 seconds before installation starts :) ")
	time.sleep(5)
	os.system(' git clone https://github.com/IAmBlackHacker/Facebook-BruteForce && git clone https://github.com/noob-hackers/ighack && git clone https://github.com/evildevill/instahack && git clone $ git clone https://github.com/dark-player/igbrute ')
	print(" Installation Over :) ")
	restart_program():


else:
	print (" ERROR : Wrong Input ")
	time.sleep(1)
	restart_program()	