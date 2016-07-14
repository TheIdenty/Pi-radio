import RPi.GPIO as GPIO
from mpd import MPDClient
from time import sleep
import re

client = MPDClient()   
client.timeout = 10 
client.idletimeout = None
client.connect("localhost", 6600)
print(client.mpd_version)

liste = client.listplaylists()

for i in liste:
    print(i['playlist'])

client.clear()
client.load(liste[2]['playlist'])
client.play()
  
  
print (liste[2])


try:
    while 1:
        sleep(1)
except KeyboardInterrupt:
    client.pause(1)
    client.close()                    
    client.disconnect()
    
  


