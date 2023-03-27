import machine
import utime

leds = [machine.Pin(22, machine.Pin.OUT), machine.Pin(21, machine.Pin.OUT), machine.Pin(20, machine.Pin.OUT)]
led_pico = machine.Pin(23, machine.Pin.OUT)

for led in leds:
    led.value(0)

i = 0
while True:
    led_pico.value(1)
    for j in range(len(leds)):
        leds[j].value((i >> j) & 1)
    i = (i + 1) % 8
    utime.sleep(1)
    led_pico.value(0)
