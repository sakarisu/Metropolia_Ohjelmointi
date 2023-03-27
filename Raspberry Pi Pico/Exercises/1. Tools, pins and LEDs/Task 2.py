import machine
import ssd1306
import utime

leds = [machine.Pin(22, machine.Pin.OUT), machine.Pin(21, machine.Pin.OUT), machine.Pin(20, machine.Pin.OUT)]
OLED_SCL = 15
OLED_SDA = 14
i2c = machine.I2C(1, scl=machine.Pin(OLED_SCL), sda=machine.Pin(OLED_SDA), freq=400000)
OLED_WIDTH = 128
OLED_HEIGHT = 64
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)


for led in leds:
    led.value(0)

i = 0
while True:
    oled.fill(1)
    oled.show()
    for j in range(len(leds)):
        leds[j].value((i >> j) & 1)
    i = (i + 1) % 8
    utime.sleep(1)
    oled.fill(0)
    oled.show()
