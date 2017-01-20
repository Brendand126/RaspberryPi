import datetime
import os

from gpiozero import PWMLED
from gpiozero import Button
from time import sleep

gp4 = PWMLED(4)
gp17 = PWMLED(17)
gp27 = PWMLED(27)
gp22 = PWMLED(22)
gp5 = PWMLED(5)
gp6 = PWMLED(6)
gp13 = PWMLED(13)
gp19 = PWMLED(19)
gp26 = PWMLED(26)
gp16 = PWMLED(16)
gp20 = PWMLED(20)
gp21 = PWMLED(21)
button = Button(23)

x = 0
h1 = 0
m1 = 0
min = 00
hour = 8

def run():
    gp4.value=0.1
    gp17.value=0.1
    gp27.value=0.1
    gp22.value=0.1
    gp5.value=0.1
    gp6.value=0.1
    gp13.value=0.1
    gp19.value=0.1
    gp26.value=0.1
    gp16.value=0.1
    gp20.value=0.1
    gp21.value=0.1
    sleep(150)
    gp4.value=0.2
    gp17.value=0.2
    gp27.value=0.2
    gp22.value=0.2
    gp5.value=0.2
    gp6.value=0.2
    gp13.value=0.2
    gp19.value=0.2
    gp26.value=0.2
    gp16.value=0.2
    gp20.value=0.2
    gp21.value=0.2
    sleep(150)
    gp4.value=0.3
    gp17.value=0.3
    gp27.value=0.3
    gp22.value=0.3
    gp5.value=0.3
    gp6.value=0.3
    gp13.value=0.3
    gp19.value=0.3
    gp26.value=0.3
    gp16.value=0.3
    gp20.value=0.3
    gp21.value=0.3
    sleep(150)
    gp4.value=0.4
    gp17.value=0.4
    gp27.value=0.4
    gp22.value=0.4
    gp5.value=0.4
    gp6.value=0.4
    gp13.value=0.4
    gp19.value=0.4
    gp26.value=0.4
    gp16.value=0.4
    gp20.value=0.4
    gp21.value=0.4
    sleep(150)
    gp4.value=0.5
    gp17.value=0.5
    gp27.value=0.5
    gp22.value=0.5
    gp5.value=0.5
    gp6.value=0.5
    gp13.value=0.5
    gp19.value=0.5
    gp26.value=0.5
    gp16.value=0.5
    gp20.value=0.5
    gp21.value=0.5
    sleep(150)
    gp4.value=0.6
    gp17.value=0.6
    gp27.value=0.6
    gp22.value=0.6
    gp5.value=0.6
    gp6.value=0.6
    gp13.value=0.6
    gp19.value=0.6
    gp26.value=0.6
    gp16.value=0.6
    gp20.value=0.6
    gp21.value=0.6
    sleep(150)
    gp4.value=0.7
    gp17.value=0.7
    gp27.value=0.7
    gp22.value=0.7
    gp5.value=0.7
    gp6.value=0.7
    gp13.value=0.7
    gp19.value=0.7
    gp26.value=0.7
    gp16.value=0.7
    gp20.value=0.7
    gp21.value=0.7
    sleep(150)
    gp4.value=0.8
    gp17.value=0.8
    gp27.value=0.8
    gp22.value=0.8
    gp5.value=0.8
    gp6.value=0.8
    gp13.value=0.8
    gp19.value=0.8
    gp26.value=0.8
    gp16.value=0.8
    gp20.value=0.8
    gp21.value=0.8
    sleep(150)
    gp4.value=0.9
    gp17.value=0.9
    gp27.value=0.9
    gp22.value=0.9
    gp5.value=0.9
    gp6.value=0.9
    gp13.value=0.9
    gp19.value=0.9
    gp26.value=0.9
    gp16.value=0.9
    gp20.value=0.9
    gp21.value=0.9
    sleep(150)
    gp4.value=1
    gp17.value=1
    gp27.value=1
    gp22.value=1
    gp5.value=1
    gp6.value=1
    gp13.value=1
    gp19.value=1
    gp26.value=1
    gp16.value=1
    gp20.value=1
    gp21.value=1


while (x<1):
    CurTime = datetime.datetime.now()
    h1 = CurTime.hour
    m1 = CurTime.minute
    if((m1==min) & (h1==hour)):
        x = x+1
        run()
    else:
        sleep(60)
        

button.wait_for_press()
gp4.value=0
gp17.value=0
gp27.value=0
gp22.value=0
gp5.value=0
gp6.value=0
gp13.value=0
gp19.value=0
gp26.value=0
gp16.value=0
gp20.value=0
gp21.value=0
sleep(2)

os.system("shutdown now -h")
