from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, sda=Pin(14), scl=Pin(15))
oled = SSD1306_I2C(128, 64, i2c)

leds = [Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(20, Pin.OUT)]
sw = [Pin(9, Pin.IN, Pin.PULL_UP), Pin(8, Pin.IN, Pin.PULL_UP), Pin(7, Pin.IN, Pin.PULL_UP)]
rotary = Pin(12, Pin.IN, Pin.PULL_UP)

leds_states = [0, 0, 0]
    
def updateDisplay():
    oled.fill(0)
    for i in range(len(leds)):
        oled.text("LED {}: {}".format(i+1, "On" if leds_states[i] else "Off"), 0, i*10)
    oled.show()
    
def interrupt(pin):
    global leds_states
    leds_states = [0, 0, 0]
    for led in leds:
        led.value(0)
    
rotary.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)

while True:
    for i in range(len(sw)):
        if not sw[i].value():
            leds_states[i] = not leds_states[i]
            leds[i].value(leds_states[i])
            updateDisplay()
            while not sw[i].value():
                pass
