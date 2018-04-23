import board
import busio as io

i2c = io.I2C(board.SCL, board.SDA)

import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)