import pyb
import random

yellow_led = pyb.LED(3)
blue_led = pyb.LED(4)

while True:

    yellow_led.intensity(random.randint(0,255))
    blue_led.intensity(random.randint(0,255))
    pyb.delay(20)