#!/usr/bin/env python

############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################

import time
import Adafruit_DHT
from beebotte import *

### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT('c168c9de01b17a29cf151bab0705dff7', 'dcd2af210e49bacd4c30b1b7db029682e01fa779d4a519ed6c37e77ac809c01a')

period = 60 ## Sensor data reporting period (1 minute)
pin = 22 ## Assuming the DHT11 sensor is connected to GPIO pin number 4

### Change channel name and resource names as suits you
temp_resource   = Resource(bbt, 'Baby_Monitor', 'Temperature')
humid_resource  = Resource(bbt, 'Baby_Monitor', 'Humidity')

def run():
  while True:
    ### Assume 
    humidity, temperature = Adafruit_DHT.read_retry( Adafruit_DHT.DHT22, pin )
    if humidity is not None and temperature is not None:
        print "Temp={0:f}*C  Humidity={1:f}%".format(temperature, humidity)
        try:
          #Send temperature to Beebotte
          temp_resource.write(temperature)
          #Send humidity to Beebotte
          humid_resource.write(humidity)
        except Exception:
          ## Process exception here
          print "Error while writing to Beebotte"
    else:
        print "Failed to get reading. Try again!"

    #Sleep some time
    time.sleep( period )

run()
