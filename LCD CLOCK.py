#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import os
import time
import lirc
from gpiozero import LED
sockid = lirc.init("remote", blocking = False)

from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

x= True
while True:
    while (x==True):
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
        codeIR = lirc.nextcode()
        if codeIR:
            x = codeIR[0]
            if (x == "2"):
                x = False
                lcd.clear()
    while (x==False):
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Hello World!")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("You are awesome")
        codeIR = lirc.nextcode()
        if codeIR:
            x = codeIR[0]
            if (x == "2"):
                x = True
                lcd.clear()
