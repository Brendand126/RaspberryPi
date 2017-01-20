from gpiozero import Buzzer, Button
from time import sleep
from signal import pause


button = Button(21)
buzzer = Buzzer(18)



button.when_pressed = buzzer.on
button.when_released = buzzer.off

pause()


