import pyb

user_switch = pyb.Switch()
user_switch.callback(lambda: pyb.LED(4).toggle())