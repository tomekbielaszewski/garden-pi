#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument used:', str(sys.argv)

# This little script provides an easy way to open the electrical relays connected
# to RPi using command:
# python watering.py 60 0
# It will export GPIO pins (defined below) as output pins, put them on HIGH state
# (we are using LOW-enabled relays) and then switch the chosen relay for give amount
# of seconds and put it back HIGH

# GPIO | Relay
#--------------
# 26     01
# 21     02
# 20     03
# 19     04
# 16     05
# 13     06
# 06     07
# 05     08

if len(sys.argv) != 3:
  print 'Argument used: ', str(sys.argv)
  print 'Watering script needs 2 arguments! Time in seconds and the relay number. Example:'
  print 'python watering.py 60 0'
  print 'This will enable first relay (index 0) for 60 seconds'
  sys.exit()

wateringTime = sys.argv[1]
relayId = sys.argv[2]

if relayId < 0 or relayId > 7:
  print 'Argument used: ', str(sys.argv)
  print 'Relay number has to be between 0 and 7'
  sys.exit()

if wateringTime < 0:
  print 'Argument used: ', str(sys.argv)
  print 'Time of opened relay has to be positive'
  sys.exit()

GPIO.setmode(GPIO.BCM)
gpioList = [26, 21, 20, 19, 16, 13, 6, 5]
relayGpio = gpioList[relayId]

for i in gpioList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH)

try:
  GPIO.output(relayGpio, GPIO.LOW)
  time.sleep(wateringTime)
  GPIO.output(relayGpio, GPIO.HIGH)
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()