import machine
import utime

leds = [machine.Pin(22, machine.Pin.OUT), machine.Pin(21, machine.Pin.OUT), machine.Pin(20, machine.Pin.OUT)]

for led in leds:
    led.value(0) 
    
while True:
    utime.sleep(1)
    for led_index in range(len(leds)):
        leds[led_index].value(1)
        utime.sleep(1)
        leds[led_index].value(0)
