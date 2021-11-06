import gc
print(gc.mem_free())

from machine import Pin
from machine import deepsleep
from machine import RTC
#from machine import nvs_setint
#from machine import nvs_getint
import time
import esp32
while(1):
 #print('T: ', (esp32.raw_temperature() - 32)*5/9)
 print('H: ', esp32.hall_sensor())

#nvs_setint('myvar', 12345678)
#sprint(nvs_getint('myvar'))

rtc = RTC()
#rtc.datetime((2021, 11, 6, 7, 14, 54, 32, 36))

print(rtc.memory());
rtcCnt=int.from_bytes(rtc.memory(), 'big');
rtcCnt+=1;
rtc.memory(rtcCnt.to_bytes(4, 'big'))
print(rtc.memory());

from machine import ADC
adc = ADC(Pin(32))
print(adc.read())

led = Pin(2, Pin.OUT, None)
led.value(0) # turn light off
#time.sleep(25)

def blink(led):
    led.value(1)
    time.sleep(1)
    led.value(0)
    led = Pin(2, Pin.OUT, Pin.PULL_HOLD)
    print(gc.mem_free())
    deepsleep(1000)

blink(led)
