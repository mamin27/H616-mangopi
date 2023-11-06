#!/usr/bin/python3

import orangepi.zero2
import OPi.GPIO as GPIO 
from time import sleep

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(orangepi.zero2.BOARD) 
GPIO.setup(10, GPIO.OUT)     

GPIO.output(10, GPIO.HIGH)

sleep(10)

GPIO.output(10, GPIO.LOW)

GPIO.cleanup()
