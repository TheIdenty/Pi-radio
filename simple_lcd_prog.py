from time import sleep
from RPLCD import CharLCD
lcd = CharLCD(cols=20, rows=2, pin_rs=10, pin_e=36, pins_data=[40, 15, 16, 18])
lcd.clear()
lcd.write_string("Hello World")
for i in range(0,10000):
    lcd.cursor_pos = (0,0)
    lcd.write_string(str(i))
    print(i)
    sleep(1)

