import board
import time
import busio as io

i2c = io.I2C(board.SCL, board.SDA)

import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

for i in range(0,3,1):
    oled.text("Starting.",0,0)
    oled.show()
    time.sleep(1)
    oled.text("Starting..",0,0)
    oled.show()
    time.sleep(1)
    oled.text("Starting...",0,0)
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.show()

for i in range(0,3,1):
    oled.text("Hello World",0,0)
    oled.show()
    oled.invert(True)
    time.sleep(1)
    oled.invert(False)
    time.sleep(1)
