import os, sys, time
from time import sleep
time.sleep(2)
print(" Hello DOXGOD We have everything you'll need ready ")
os.system(' clear ')
print ("         @pwn.doxgod Like It So Far?                       ")
time.sleep(0.3)
print ("██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗   ")
time.sleep(0.3)
print ("██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝   ")
time.sleep(0.3)
print ("██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗  ")
time.sleep(0.3)
print (" ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║  ")
time.sleep(0.3)
print ("██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝  ")
time.sleep(0.3)
print ("╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝   ")
time.sleep(0.3)                                                         
print (" [01]> Socialfish:                                         ")
time.sleep(0.3)
print (" [02]> ZPhisher:                                           ")
time.sleep(0.3)
print (" [03]> NexPhisher:                                         ")
time.sleep(0.3)
print (" [04]> Sooty:                                              ")
time.sleep(0.3)
print (" [05]> EvilURL:                                            ")
time.sleep(0.3)
print (" [06]> Blackeye:                                           ")
time.sleep(0.3)
print (" [07]> Hiddeneye:                                          ")
time.sleep(0.3)
print (" [08] Install Tools                                        ")
Phish = input(" Phishing  ==>> ")
if Phish == '01' or Phish == '1':
	os.system(' clear ')
	os.system(' cd SocialFish && pip3 install -r requirements.txt && python3 SocialFish.py ')
elif Phish == '02' or Phish == '2':
	os.system(' clear ')
	os.system(' cd zphisher && bash zphisher.sh ')
elif Phish == '03' or Phish == '3':
	os.system(' clear ')
	os.system(' cd nexphisher && bash nexphisher ')

elif Phish == '04' or Phish == '4':
  os.system(' clear ')
  os.system(' cd Sooty && pip3 install -r requirements.txt && python3 Sooty.py ')

elif Phish == '05' or Phish == '5':
  os.system(' clear ')
  os.system(' cd EvilURL && python3 evilurl.py && python3 evilurl-cli.py ')
  
elif Phish == '06' or Phish == '6':
  os.system(' clear ')
  os.system(' cd blackeye && sudo ./blackeye.sh ')
  
elif Phish == '07' or Phish == '7':
  os.system(' clear ')
  os.system(' cd HiddenEye && pip3 install -r requirements.txt && python3 HiddenEye.py ')
 
elif Phish == '08' or Phish == '8':
	os.system(' clear ')
	os.system(' git clone https://github.com/UndeadSec/EvilURL && git clone https://github.com/UndeadSec/SocialFish && git clone https://github.com/htr-tech/zphisher && https://github.com/htr-tech/nexphisher && git clone https://github.com/TheresAFewConors/Sooty && git clone https://github.com/An0nUD4Y/blackeye && git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy ')
	os.system(' clear ')
	os.system(' python3 beens.py ')

else:
      print (" \nERROR: Wrong Input ")
      timeout(3)
      restart_program()
