# -*- coding: utf-8 -*-
# Copyright (c) 2022 sillo01
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Zero2
(see https://linux-sunxi.org/File:Orange_Pi_Zero2_H616_Schematic_v1.3.pdf)
Usage:
.. code:: python
   import orangepi.zero2
   from OPi import GPIO
   GPIO.setmode(orangepi.zero2.BOARD)
 +------+-----+----------+------+---+   H616   +---+------+----------+-----+------+
 | GPIO | wPi |   Name   | Mode | V | Physical | V | Mode | Name     | wPi | GPIO |
 +------+-----+----------+------+---+----++----+---+------+----------+-----+------+
 |      |     |     3.3V |      |   |  1 || 2  |   |      | 5V       |     |      |
 |  229 |   0 |    SDA.3 | ALT5 | 0 |  3 || 4  |   |      | 5V       |     |      |
 |  228 |   1 |    SCL.3 | ALT5 | 0 |  5 || 6  |   |      | GND      |     |      |
 |   73 |   2 |      PC9 |  OFF | 0 |  7 || 8  | 0 | OFF  | TXD.5    | 3   | 226  |
 |      |     |      GND |      |   |  9 || 10 | 0 | ALT4 | RXD.5    | 4   | 227  |
 |   70 |   5 |      PC6 | ALT5 | 0 | 11 || 12 | 0 | OFF  | PC11     | 6   | 75   |
 |   69 |   7 |      PC5 | ALT5 | 0 | 13 || 14 |   |      | GND      |     |      |
 |   72 |   8 |      PC8 |  OFF | 0 | 15 || 16 | 0 | OFF  | PC15     | 9   | 79   |
 |      |     |     3.3V |      |   | 17 || 18 | 0 | OFF  | PC14     | 10  | 78   |
 |  231 |  11 |   MOSI.1 |  OFF | 0 | 19 || 20 |   |      | GND      |     |      |
 |  232 |  12 |   MISO.1 |  OFF | 0 | 21 || 22 | 0 | OFF  | PC7      | 13  | 71   |
 |  230 |  14 |   SCLK.1 |  OFF | 0 | 23 || 24 | 0 | OFF  | CE.1     | 15  | 233  |
 |      |     |      GND |      |   | 25 || 26 | 0 | OFF  | PC10     | 16  | 74   |
 |   65 |  17 |      PC1 |  OFF | 0 | 27 || 28 |   |      |          |     |      |
 |  272 |  18 |     PI16 | ALT2 | 0 | 29 || 30 |   |      |          |     |      |
 |  262 |  19 |      PI6 |  OFF | 0 | 31 || 32 |   |      |          |     |      |
 |  234 |  20 |     PH10 | ALT3 | 0 | 33 || 34 |   |      |          |     |      |
 +------+-----+----------+------+---+----++----+---+------+----------+-----+------+
 | GPIO | wPi |   Name   | Mode | V | Physical | V | Mode | Name     | wPi | GPIO |
 +------+-----+----------+------+---+   H616   +---+------+----------+-----+------+
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi Zero 2 physical board pin to GPIO pin
BOARD = {
    3:    229,   # PH5/I2C3_SDA
    5:    228,   # PH4/I2C3_SCK
    7:    73,    # PC9
    8:    226,   # PH2/UART5_TX
    10:   227,   # PH3/UART5_RX
    11:   70,    # PC6
    12:   75,    # PC11
    13:   69,    # PC5
    15:   72,    # PC8
    16:   79,    # PC15
    18:   78,    # PC14
    19:   231,   # PH7,SPI1_MOSI
    21:   232,   # PH8,SPI1_MISO
    22:   71,    # PC7
    23:   230,   # PH6,SPI1_CLK
    24:   233,   # PH9,SPI1_CS
    26:   74,    # PC10
    27:   65,    # PC1
    29:  272,    # PI16
    31:  262,    # PI6
    33:  234,    # PH10
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
