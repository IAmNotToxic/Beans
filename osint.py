import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ') 
print(" ██████╗ ███████╗██╗███╗   ██╗████████╗ ")   
time.sleep(0.1)
print("██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝ ")   
time.sleep(0.1)
print("██║   ██║███████╗██║██╔██╗ ██║   ██║    ")   
time.sleep(0.1)
print("██║   ██║╚════██║██║██║╚██╗██║   ██║    ")     
time.sleep(0.1)
print("╚██████╔╝███████║██║██║ ╚████║   ██║    ")  
time.sleep(0.1)
print(" ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝    ") 
time.sleep(0.1)
print("    A Sherlock:      ")
time.sleep(0.1)
print("     B GHunt:		")
time.sleep(0.1)
print("     C SpiderFoot:   ")
time.sleep(0.1)
print("     D Instaloader:  ")
time.sleep(0.1)
print("     E OSINT: 		")
time.sleep(0.1)
print("     F Install:   	")

osint = input(" OSINT ==>> ")

if osint == 'A' or 'a':
	os.system(' clear ')
	X = str(input(" Type Username:"))
	os.system(' cd sherlock && python3 sherlock.py X ')

if osint == 'B' or 'b':
	os.system(' clear ')
	os.system(' cd GHunt && python3 ghunt.py ')

if osint == 'C' or 'c':
	os.system(' clear ')
	os.system(' cd spiderfoot && pip3 install -r requirements.txt && python3 ./sy.py ')

if osint == 'D' or 'd':
	os.system(' clear ')
	os.system(' cd instaloader && python3 instaloader ')

if osint == 'E' or 'e':
	os.system(' clear ')
	os.system(' cd Osintgram && pip3 install -r requirements.txt && python3 main.py ')

if osint == 'F' or 'f':
	os.system(' clear ')
	print(Fore.WHITE+" Wait 5 Seconds :) ")
	os.system(' git clone https://github.com/sherlock-project/sherlock.git && git clone https://github.com/mxrch/GHunt && git clone https://github.com/smicallef/spiderfoot && git clone https://github.com/instaloader/instaloader && git clone https://github.com/Datalux/Osintgram ')			
