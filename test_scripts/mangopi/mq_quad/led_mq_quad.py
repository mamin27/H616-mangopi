#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mangopi.mq_quad
import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

GPIO.setmode(mangopi.mq_quad.BOARD)        # set up BOARD MangoPi MQ-QUAD pin numbering
GPIO.setup(41, GPIO.OUT)         # set MangoPi (LED status) as an output

try:
    print ("Press CTRL+C to exit")
    while True:
        GPIO.output(41, 1)       # set port/pin value to 1/HIGH/True
        sleep(0.1)
        GPIO.output(41, 0)       # set port/pin value to 0/LOW/False
        sleep(0.1)

        GPIO.output(41, 1)       # set port/pin value to 1/HIGH/True
        sleep(0.1)
        GPIO.output(41, 0)       # set port/pin value to 0/LOW/False
        sleep(0.1)

        sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(41, 0)           # set port/pin value to 0/LOW/False
    GPIO.cleanup()              # Clean GPIO
    print ("Bye.")

