from gpiozero import LED
from time import sleep

gp17 = LED(17)
gp27 = LED(27)
gp22 = LED(22)
gp5 = LED(5)
gp6 = LED(6)
gp13 = LED(13)
gp19 = LED(19)
gp26 = LED(26)

x = 1
while(x < 10):
    gp17.on()
    gp19.on()
    gp5.on()
    sleep(0.05)
    sleep(0.02)
    gp17.off()
    sleep(0.02)
    gp17.off()
    gp13.on()
    gp6.on()
    sleep(0.06)
    gp13.off()
    gp17.on()
    sleep(0.06)
    gp26.on()
    sleep(0.03)
    gp17.off()
    sleep(0.03)
    gp19.on()
    gp5.off()
    gp26.off()
    sleep(0.05)
    gp13.on()
    gp19.off()
    sleep(0.04)
    gp22.on()
    gp6.off()
    sleep(0.08)
    gp22.off()
    sleep(0.02)
    gp26.on()
    gp13.off()
    gp19.off
    sleep(0.03)
    gp27.on()
    sleep(0.08)
    gp26.off()
    gp27.off()
    x = x+1

sleep(2)
gp5.on()
sleep(1.5)
gp5.off()
sleep(2)
gp22.on()
sleep(1.5)
gp22.off()
sleep(3)
gp13.on()
    
