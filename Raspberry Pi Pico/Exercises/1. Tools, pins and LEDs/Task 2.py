import machine
import ssd1306
import utime

leds = [machine.Pin(22, machine.Pin.OUT), machine.Pin(21, machine.Pin.OUT), machine.Pin(20, machine.Pin.OUT)]
i2c = machine.I2C(1, scl=machine.Pin(15), sda=machine.Pin(14), freq=200000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


for led in leds:
    led.value(0)

i = 0
while True:
    oled.fill(1)
    for j in range(len(leds)):
        leds[j].value((i >> j) & 1)
    i = (i + 1) % 8
    utime.sleep(1)
    oled.fill(0)
