from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime


testSet1 = [1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100,
              1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100]
testSet2 = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812,
              812, 756, 820, 812, 800]

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

def calcHrvParameters(ppiVal):
    meanPpi = sum(ppiVal) / len(ppiVal)
    meanHr = 60000 / meanPpi
    sdnn = (sum([(ppi - meanPpi) ** 2 for ppi in ppiVal]) / len(ppiVal)) ** 0.5
    rmssd = (sum([(ppiVal[i] - ppiVal[i-1]) ** 2 for i in range(1, len(ppiVal))]) / (len(ppiVal) - 1)) ** 0.5
    return meanPpi, meanHr, sdnn, rmssd

meanPpi1, meanHr1, sdnn1, rmssd1 = calcHrvParameters(testSet1)
meanPpi2, meanHr2, sdnn2, rmssd2 = calcHrvParameters(testSet2)

def updateDisplay(testSet):
    oled.fill(0)
    oled.text("Test Set", 0, 0)
    oled.text("Mean PPI: {:.2f}".format(testSet[0]), 0, 10)
    oled.text("Mean HR: {:.2f}".format(testSet[1]), 0, 20)
    oled.text("SDNN: {:.2f}".format(testSet[2]), 0, 30)
    oled.text("RMSSD: {:.2f}".format(testSet[3]), 0, 40)
    oled.show()

currTestSet = 1
while True:
    if currTestSet == 1:
        updateDisplay([meanPpi1, meanHr1, sdnn1, rmssd1])
        currTestSet = 2
    else:
        updateDisplay([meanPpi2, meanHr2, sdnn2, rmssd2])
        currTestSet = 1      
    utime.sleep(5)#OLED display switches between test sets 1 and 2 every 5 seconds
