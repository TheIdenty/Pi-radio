from time import sleep
from RPLCD import CharLCD
from math import *
import RPi.GPIO as GPIO
from mpd import MPDClient
import re

GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
col = 20
row = 2
index_0 = 0
index_1 = 0
menu_level = 0
playlists = []

#sleep(60) #wait for mopidy to start

client = MPDClient()   
client.timeout = 10 
client.idletimeout = None
print "Hello"
client.connect("localhost", 6600)


print(client.mpd_version)

lcd = CharLCD(cols=col, rows=row, pin_rs=10, pin_e=36, pins_data=[40, 15, 16, 18])

eintraege = ["play", "pause", "playlists", "test4", "test5"]

def list_down(channel):
    global index_0
    global index_1
    global menu_level
    if menu_level == 0:
        index_0 = (index_0 + 1) % 5
        menu_0(index_0)
    elif menu_level == 1:
        index_1 = (index_1 +1) % (len(playlists))
        menu_1(index_1)
        

def list_enter(channel):
    global index_0
    global playlists
    global menu_level
    lcd.clear()
    if menu_level == 0:
        if index_0 == 0:
            lcd.write_string("Play")
            client.pause(0)
        elif index_0 == 1:
            lcd.write_string("Pause")
            client.pause(1)
        elif index_0 == 2:
            playlists_raw1 = client.listplaylists()
            menu_level = 1
            del playlists[:]
            for i in playlists_raw1:
                playlists.append(i['playlist'])
            menu_1(0)
        else:
            lcd.write_string("nothing")
    elif menu_level == 1:
        client.pause(1)
        client.clear()
        client.load(playlists[index_1])
        client.play()
        
def menu_0(pos):
    global eintraege
    global row
    lcd.clear()
    for i in range (0, row):
        lcd.cursor_pos = (i,0)
        lcd.write_string(eintraege[(pos+i)%len(eintraege)])
 
def menu_1(pos):
    global row
    global playlists
    lcd.clear()
    for i in range (0, row):
        lcd.cursor_pos = (i,0)
        lcd.write_string(playlists[(pos+i)%len(playlists)][0:19]) 
    

GPIO.add_event_detect(33, GPIO.FALLING, callback=list_down, bouncetime=100)
GPIO.add_event_detect(35, GPIO.FALLING, callback=list_enter, bouncetime=100)
 

 
menu_0(0)



try:
    while 1:
        sleep(1)
except KeyboardInterrupt:
    lcd.clear()
    lcd.close()
    client.close()                    
    client.disconnect()
  
 
#lcd.clear()
#lcd.close()
#client.close()                    
#client.disconnect()

#print('Test done.')


