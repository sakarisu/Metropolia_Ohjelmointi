from machine import I2C, Pin, PWM
from ssd1306 import SSD1306_I2C
from led import Led
import utime

class ledMenu:
    def __init__(self, rota, rotb, rotbtn, leds):
        self.rotA = rota
        self.rotA.irq(trigger=Pin.IRQ_RISING, handler=self.rotate)
        self.rotB = rotb
        self.rotB.irq(trigger=Pin.IRQ_RISING, handler=self.rotate)
        self.rotBtn = rotbtn
        self.rotBtn.irq(handler=self.switchLed, trigger=Pin.IRQ_FALLING)
        self.leds = leds
        self.aled = 0
        self.mode = 1

    def rotate(self, pin):
        arvo = int((self.leds[self.aled]._on_val / 65535) * 100 + 0.5)
        if pin == self.rotA:
            if not self.rotB.value():
                if arvo == 1:
                    self.leds[self.aled].value(1)
                self.leds[self.aled].brightness(arvo + 1)
            else:
                if arvo == 1:
                    self.leds[self.aled].value(0)
                self.leds[self.aled].brightness(arvo - 1)
        else:
            if self.rotA.value():
                if arvo == 1:
                    self.leds[self.aled].value(1)
                self.leds[self.aled].brightness(arvo + 1)
            else:
                if arvo == 1:
                    self.leds[self.aled].value(0)
                self.leds[self.aled].brightness(arvo - 1)

    def switchLed(self, pin):
        utime.sleep_ms(20)
        if not pin.value():
            self.aled = (self.aled + 1) % 3
            
rota = Pin(10, Pin.IN, pull=Pin.PULL_UP)
rotb = Pin(11, Pin.IN, pull=Pin.PULL_UP)
rotbtn = Pin(12, Pin.IN, pull=Pin.PULL_UP)
leds = [Led(22), Led(21), Led(20)]
menu = ledMenu(rota, rotb, rotbtn, leds)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)       
oled = SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text("LED: {}".format(menu.aled + 1), 0, 0)
    brightPer = int((menu.leds[menu.aled]._on_val / 65535) * 100)
    barWidth = int(brightPer / 10)
    oled.rect(0, 16, 120, 8, 1)
    oled.fill_rect(2, 18, barWidth * 12, 4, 1)
    oled.show()
    utime.sleep(0.1)
