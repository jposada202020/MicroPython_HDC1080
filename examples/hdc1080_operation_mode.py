# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_hdc1080 import hdc1080

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
hdc = hdc1080.HDC1080(i2c)

hdc.operation_mode = hdc1080.TEMP_OR_HUM

while True:
    for operation_mode in hdc1080.operation_mode_values:
        print("Current Operation mode setting: ", hdc.operation_mode)
        for _ in range(10):
            print(f"Temperature: {hdc.temperature:.2f}°C")
            print()
            time.sleep(0.5)
        hdc.operation_mode = operation_mode
