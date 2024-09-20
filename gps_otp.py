import utime
import random

from machine import I2C,UART, Pin

import time

import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME
import time

#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect("slabs", "12345678")
print("Connecting..")
while not GLOB_WLAN.isconnected():
  print(".")
  time.sleep(2)
  
print("Connected")
#firebase example
import ufirebase as firebase
firebase.setURL("https://arcontrol-fcc95-default-rtdb.firebaseio.com/")
#firebase.setURL("https://prayana-ev-default-rtdb.asia-southeast1.firebasedatabase.app/")
buff = bytearray(255)

TIMEOUT = False
FIX_STATUS = False
 

#Generation and sending OTP to Firebase
otp = random.randint(1111,9999)
print(otp)
firebase.put("prayanaelectric/OTP", otp, bg = 0)


from oldgps.py import latitude, longitude
#firebase.put("ASHOK_LOC1", str(info[2])+","+str(info[3]), bg=0)

