#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
   # Main loop
 #sleep for one second to allow the sensor to set up
 time.sleep(1)
 #convert the resistance value to lux and print it  
 lux=("%.2f" % (10000.0/(pow((rc_time(pin_to_circuit)/100.0),4/3.0))))
 #store data in json format
 data={"Illumination(lux)":lux}
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
