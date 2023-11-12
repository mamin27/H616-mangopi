**Dont forget to add ![/image/star.png](https://github.com/mamin27/ecomet_i2c_raspberry_tools/blob/master/python_test_scripts/display/images/star.png) if you were satisfy with the software!**

# H616-mangopi (version 1.2)
DTS file for setting MQ-Quad / MCore-H616 board

[MQ-Quad H616](https://mangopi.org/mqquad)
# Compile DTS fit to DTB binary and reboot

```ps
sudo apt-get install sunxi-tools device-tree-compiler rpi.gpio-common

cd /boot/dtb/allwinner/
dtc -I dts -O dtb -f sun50i-h616-biqu.dts -o sun50i-h616-biqu.dtb
```
# OPi.GPIO package for H616 board (my clone of origin library)
* current version 0.5.4 (added some not applied pull-request from origin https://github.com/rm-hull/OPi.GPIO project & my changes)
* this version is not distributed by pypi.org, I respect owner of the project.
* Added mangopi library
* How to compile lib:
```ps
cd OPi.GPIO
sudo bin/make_release.sh
cd dist
pip3 install OPi.GPIO-0.5.4-py2.py3-none-any.whl
```
* test of flashing LED
```ps
./led_mq_quad.py
```

### features:
* I2C (/dev/i2c-1)
* SPI
* PWM
  - for correct using PWM install OPi.GPIO lib from this site
  - test script for managing PWM was tested at OrangePi Zero2 [fan_pwm_managed script](https://github.com/mamin27/H616-mangopi/tree/main/test_scripts/orangepi/zero2)
* GPIO INPUT/OUTPU
  - test script for managing PIN status was tested at OrangePi Zero2 [fan_gpio_managed script](https://github.com/mamin27/H616-mangopi/tree/main/test_scripts/orangepi/zero2)
* I2S0 TBD (Look at issue #1 and help with investigatio)
* activate sensor-led TBD


```ps
comet@mangopi:/boot/dtb/allwinner$ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: 50 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- 62 -- -- -- -- -- -- -- -- -- -- -- -- --
70: 70 -- -- -- -- -- -- --
```
