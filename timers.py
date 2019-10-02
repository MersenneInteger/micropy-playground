import pyb

##timers
timer = pyb.Timer(4)
#initialize and set frequency to 10Hz
timer.init(freq=10)
#print timer in REPL yields: 
# Timer(4, freq=10, prescaler=624, period=13439, mode=UP, div=1)
# which means that peripheral clock speed is divided by 624+1 and will count
# from 0 to 13439 and start over
# the source freq is 84MHz so 84000000/625/13440 = 10 Hz

#print current timer value
#timer.counter()

#flash the red LED at 5Hz
timer.callback(lambda t: pyb.LED(1).toggle())

#create timer obj
timer7 = pyb.Timer(7)
#initialize timer to 2Hz
timer7.init(freq=2)
#oscillate green LED at 1Hz
timer7.callback(lambda t: pyb.LED(2).toggle())