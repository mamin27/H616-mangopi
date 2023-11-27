#!/usr/bin/python3

import orangepi.zero2
import OPi.GPIO as GPIO 
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(orangepi.zero2.BOARD) 

PWM_chip = 0
PWM_pin = 1
frequency_Hz = 31
Duty_Cycle_Percent = 100 


pwm = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)
print('turn on pwm by pressing button')
input()
pwm.start_pwm()

#print('dimm pwm by pressing button')
#input()
for i in [26,50,75,100]:
   pwm.duty_cycle(i)
   print ("Duty cycle: " + str(i))
   sleep(10)

#print('change pwm frequency by pressing button')
#input()
#pwm.change_frequency(2000)

#print('stop pwm by reducing duty cycle to 0 by pressing button')
#input()
#pwm.stop_pwm()

#print('increase duty cycle but inverted so light will dim. press button')
#input()

#for i in range(10,99):
#   pwm.duty_cycle(i)
#   print ("Duty cycle: " + str(i))
#   sleep(5)

#print('stop pwm (it was inverted so it should be full brightness), press button')
pwm.stop_pwm()

#print('remove object and deactivate pwm pin, press button')
#input()
pwm.pwm_close()

del pwm

GPIO.cleanup()


