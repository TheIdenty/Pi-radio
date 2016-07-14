from Rotary_class import RotaryEncoder
import time

PIN_A = 4
PIN_B = 17
BUTTON = 27

def switch_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        print "CLOCKWISE"
    elif event == RotaryEncoder.ANTICLOCKWISE:
        print "ANTiclockwise"
    elif event == RotaryEncoder.BUTTONDOWN:
        print "Button down"
    elif event == RotaryEncoder.BOTTONUP:
        print "Button up"

rswitch = RotaryEncoder(PIN_A, PIN_B, BUTTON, switch_event)        
        
while True:
    time.sleep(0.5)