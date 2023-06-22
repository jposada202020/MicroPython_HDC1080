# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_hdc1080 import hdc1080

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
hdc = hdc1080.HDC1080(i2c)

hdc.humidity_resolution = hdc1080.HUM_RES_11BIT

while True:
    for humidity_resolution in hdc1080.humidity_resolution_values:
        print("Current Humidity resolution setting: ", hdc.humidity_resolution)
        for _ in range(10):
            temp = hdc.temperature
            print("Temperature: {:.2f}C".format(temp))
            print()
            time.sleep(0.5)
        hdc.humidity_resolution = humidity_resolution
