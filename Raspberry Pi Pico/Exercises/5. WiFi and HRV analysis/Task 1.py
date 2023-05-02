from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import network
import utime

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
ssid = 'KME670Group8'
pssw = 'or2i2hA00HVJsa1xMiIs'

def getIp(ssid, pssw):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, pssw)
    if not wlan.isconnected():
        print("Connecting...")
        wlan.connect(ssid, pssw)
        while not wlan.isconnected():
            pass
    print('Connected!')
    return wlan.ifconfig()[0]

oled.fill(0)
oled.text('IP:', 0, 0)
oled.text(getIp(ssid, pssw), 0, 20)
oled.show()
