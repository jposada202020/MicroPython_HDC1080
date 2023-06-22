# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_hdc1080 import hdc1080

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
hdc = hdc1080.HDC1080(i2c)

hdc.temperature_resolution = hdc1080.TEMP_RES_14BIT

while True:
    for temperature_resolution in hdc1080.temperature_resolution_values:
        print("Current Temperature resolution setting: ", hdc.temperature_resolution)
        for _ in range(10):
            temp = hdc.temperature
            print("Temperature: {:.2f}C".format(temp))
            print()
            time.sleep(0.5)
        hdc.temperature_resolution = temperature_resolution
