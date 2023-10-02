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
* current version 0.5.4
* Added mangopi library
* How to compile lib:
```ps
cd OPi.GPIO
sudo bin/make_release.sh
```
* test of flashing LED
```ps
./led_mq_quad.py
```

### features:
* I2C (/dev/i2c-1)
* SPI
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
