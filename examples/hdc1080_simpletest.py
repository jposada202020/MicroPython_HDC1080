# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_hdc1080 import hdc1080

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
hdc = hdc1080.HDC1080(i2c)

while True:
    temperature, humidity = hdc.measurements
    print("Temperature: {:.2f} C".format(temperature))
    print("Humidity: {:.2f} %%".format(humidity))
    print("")
    time.sleep(0.5)
