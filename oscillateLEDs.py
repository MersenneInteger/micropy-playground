import pyb

#leds = [pyb.LED(1), pyb.LED(2), pyb.LED(3), pyb.LED(4)]
leds = [pyb.LED(i) for i in range(1,5)]

try:
    while True:
        for led in leds:
            led.on()
            pyb.delay(500)
            led.off()
finally:
    for led in leds:
        led.off()