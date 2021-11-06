#https://creatronix.de/using-micropython-on-firebeetle-esp32/
from machine import Pin
import time

p2 = Pin(2, Pin.OUT)

def blink():
    while True:
        p2.value(0)
        time.sleep(1)
        p2.value(1)
        time.sleep(1)

blink()
