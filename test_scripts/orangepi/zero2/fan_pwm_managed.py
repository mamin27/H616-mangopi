#!/usr/bin/python3

import orangepi.zero2
import OPi.GPIO as GPIO 
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(orangepi.zero2.BOARD) 

PWM_chip = 0
PWM_pin = 1
frequency_Hz = 3800
Duty_Cycle_Percent = 100 


pwm = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)
print('turn on pwm by pressing button')
input()
pwm.start_pwm()

print('dimm pwm by pressing button')
input()
pwm.duty_cycle(50)

print('change pwm frequency by pressing button')
input()
pwm.change_frequency(1000)

print('stop pwm by reducing duty cycle to 0 by pressing button')
input()
pwm.stop_pwm()

print('increase duty cycle but inverted so light will dim. press button')
input()
pwm.duty_cycle(75)

print('duty cycle reduced press button to continue')
input()
pwm.duty_cycle(25)

print('stop pwm (it was inverted so it should be full brightness), press button')
input()
pwm.stop_pwm()

print('remove object and deactivate pwm pin, press button')
input()
pwm.pwm_close()

del pwm

GPIO.cleanup()
