# -*- coding: utf-8 -*-

# https://www.instructables.com/id/Using-Pm25-Sensor-With-Raspberry-Pi/
# NOVA PM sensor: documentation
# https://nettigo.pl/attachments/398

# aqi library
# https://media.readthedocs.org/pdf/python-aqi/latest/python-aqi.pdf
# pip install python-aqi

import serial # module to read data from sensor
import time # time management
import aqi # conversion to US, CN , AQI index


t = serial.Serial('com8',9600)   # modify the serial
#'/dev/ttyUSB0'



#while True:
for i in range(0,10):
    t.flushInput()
    time.sleep(0.5)
    retstr = t.read(10)
    if (len(retstr)==10):
        if(retstr[0]==0xaa and retstr[1]==0xc0):
            if sum(retstr[2:8]) % 256 == retstr[8]: # check if error occur from check-sum
                pm25  = (int(retstr[2])+int(retstr[3])*256) / 10 # in ug/m3
                pm10  = (int(retstr[4])+int(retstr[5])*256) / 10 # in ug/m3

                aqi25_us = int(aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pm25), aqi.ALGO_EPA))
                aqi25_cn = int(aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pm25), aqi.ALGO_MEP))
                
                print ("pm2.5:%.1f AQI_US: %d AQI_CN: %d"%(pm25,aqi25_us,aqi25_cn))

 
 

    
