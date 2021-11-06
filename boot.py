# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from machine import RTC
rtc = RTC()
print(rtc.datetime())
print(int.from_bytes(rtc.memory(), 'big'))

import esp32
print((esp32.raw_temperature() - 32)*5/9)
print(esp32.hall_sensor())

import esp
print(esp.flash_size())
print(esp.flash_user_start())

import machine
print(machine.unique_id())
print(machine.reset_cause(), machine.DEEPSLEEP_RESET)
print(machine.wake_reason(), machine.TIMER_WAKE)

#wdt = machine.WDT(timeout=2000)
#wdt = machine.WDT(0)
#wdt.feed()


