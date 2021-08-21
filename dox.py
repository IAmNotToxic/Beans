import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ') 
print ("$$$$$$$$\                           $$\       $$\                             $$$$$$\  $$\       $$\       $$\       $$\                        ") 
print ("\__$$  __|                          $$ |      \__|                           $$  __$$\ $$ |      \__|      $$ |      $$ |                       ") 
print ("   $$ | $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\ $$\ $$$$$$$\   $$$$$$\         $$ /  \__|$$ |  $$\ $$\  $$$$$$$ | $$$$$$$ | $$$$$$\   $$$$$$$\    ") 
print ("   $$ |$$  __$$\ \____$$\ $$  _____|$$ | $$  |$$ |$$  __$$\ $$  __$$\ $$$$$$\\$$$$$$\  $$ | $$  |$$ |$$  __$$ |$$  __$$ |$$  __$$\ $$  _____|   ") 
print ("   $$ |$$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$ |$$ |  $$ |$$ /  $$ |\______|\____$$\ $$$$$$  / $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |\$$$$$$\     ") 
print ("   $$ |$$ |     $$  __$$ |$$ |      $$  _$$<  $$ |$$ |  $$ |$$ |  $$ |       $$\   $$ |$$  _$$<  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\    ") 
print ("   $$ |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ $$ |$$ |  $$ |\$$$$$$$ |       \$$$$$$  |$$ | \$$\ $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$$$$$$  |   ") 
print ("   \__|\__|      \_______| \_______|\__|  \__|\__|\__|  \__| \____$$ |        \______/ \__|  \__|\__| \_______| \_______| \______/ \_______/    ")
print ("                                                            $$\   $$ |                                                                          ") 
print ("                                                            \$$$$$$  |                                                                          ") 
print ("                                                             \______/                                                                           ") 
print (" [01]> track-ip		")
print (" [02]> ip-tracer 	")
print (" [03]> Sigit 		")
print (" [00]> Exit		")
rebirthed = input(" Tracking-Skiddos ==>> ")
if rebirthed == '01' or rebirthed == '1':
	os.system(' clear ')
	os.system(' cd track-ip && chmod +x * && ./trackip ')

elif rebirthed == '02' or rebirthed == '2':
	os.system(' clear ')
	os.system(' cd IP-Tracer && chmod +x * && ./install ')
	
elif rebirthed == '00' or rebirthed == '0':
	os.system(' python2 alqueda.py ')
elif rebirthed == '03' or rebirthed == '3':
	os.system(' clear ')
	os.system(' cd SIGIT && bash install.sh && python3 sigit.py ')
	
else:
      print (" \nERROR: Wrong Input ")
      restart_program()