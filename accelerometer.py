import pyb

accel = pyb.Accel()

while True:

    pyb.LED(4).on() if accel.x() < 0 else pyb.LED(4).off()
    pyb.LED(3).on() if accel.y() < 0 else pyb.LED(3).off()
    pyb.LED(2).on() if accel.z() < 0 else pyb.LED(2).off()
    pyb.LED(1).on() if accel.x() > 0 else pyb.LED(1).off()
    pyb.delay()

