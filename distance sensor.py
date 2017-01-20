from gpiozero import DistanceSensor
from time import sleep
ultrasonic = DistanceSensor(echo=24, trigger=23)

while True:
    print(ultrasonic.distance)
