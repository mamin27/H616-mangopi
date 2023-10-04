# -*- coding: utf-8 -*-
# Copyright (c) 2022 sillo01
# See LICENSE.md for details.

"""
Alternative pin mappings for Mango PI MQ-QUAD with H616
(see https://mangopi.org/_media/mq-quad-sch-v1p2.pdf)
Usage:
.. code:: python
   import mangepi.mq_quad
   from OPi import GPIO
   GPIO.setmode(mangepi.mq_quad.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Mango Pi MQ-QUAD H616 physical board pin to GPIO pin
BOARD = {
    3:     263,  # PI8/TWI0-SDA
    5:     262,  # PI7/TWI0-SCK
    7:     256,  # PI0/I2S0-MCLK
    8:     224,  # PH0/TWI1-SCK/TX0
    10:    225,  # PH1/TWI1-SDA/RX0
    11:    226,  # PH2/TWI2-SCK/TX5
    12:    257,  # PI1/I2S0-BCLK
    13:    227,  # PH3/TWI2-SDA/RX5
    15:    268,  # PI13/TX4/PWM3
    16:    269,  # PI14/RX4/PWM4
    18:    228,  # PH4/SPDIF-OUT
    19:    231,  # PH7/SPI1-MOSI
    21:    232,  # PH8/SPI1-MISO
    22:    261,  # PI6/RX2
    23:    230,  # PH6/SPI1-CLK
    24:    229,  # PH5/SPI1-CSO
    26:    233,  # PH9/SPI1-CS1
    27:    265,  # PI10/TWI2-SDA
    28:    264,  # PI9/TWI2-SCK
    29:    266,  # PI11
    31:    267,  # PI12
    32:    260,  # PI5/TX2/LEDC
    33:    270,  # PI15
    35:    258,  # PI2/I2S0-LCR
    36:    234,  # PH10
    37:    271,  # PI16
    38:    260,  # PI4/I2S0-DOUT
    40:    259,  # PI3/I2S0-DIN
    41:    77,   # PC13/STATUS_LED
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
