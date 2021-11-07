import esp32
from time import sleep
t = esp32.raw_temperature
hall = esp32.hall_sensor
while(1):
 #print('T: ', (t() - 32)*5/9)
 print('H: ', hall())
 sleep(0.1)
 
 