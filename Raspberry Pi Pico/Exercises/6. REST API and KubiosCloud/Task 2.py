from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import network
import urequests
import ujson
import utime



APIKEY = "pbZRUi49X48I56oL1Lq8y8NDjq6rPfzX3AQeNo3a"
CLIENT_ID = "3pjgjdmamlj759te85icf0lucv"
CLIENT_SECRET = "111fqsli1eo7mejcrlffbklvftcnfl4keoadrdv1o45vt9pndlef"
LOGIN_URL = "https://kubioscloud.auth.eu-west-1.amazoncognito.com/login"
TOKEN_URL = "https://kubioscloud.auth.eu-west-1.amazoncognito.com/oauth2/token"
REDIRECT_URI = "https://analysis.kubioscloud.com/v1/portal/login"
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
ssid = 'KME670Group8'
pssw = 'or2i2hA00HVJsa1xMiIs'


def connection(ssid, pssw):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting...')
        wlan.connect(ssid, pssw)
        while not wlan.isconnected():
            pass
    ip = wlan.ifconfig()[0]
    print('Connected to ' + ip)


def request(intervals):
    responseToken = urequests.post(
        url = TOKEN_URL,
        data = 'grant_type=client_credentials&client_id={}'.format(CLIENT_ID),
        headers = {'Content-Type':'application/x-www-form-urlencoded'},
        auth = (CLIENT_ID, CLIENT_SECRET))
    responseToken = responseToken.json()
    accessToken = responseToken["access_token"] 
    dataset = {
        "type": "RRI",
        "data": intervals,
        "analysis": {
            "type": "readiness"}
    }
    responseData = urequests.post(
        url = "https://analysis.kubioscloud.com/v2/analytics/analyze",
        headers = { 
            "Authorization": "Bearer {}".format(accessToken), 
            "X-Api-Key": APIKEY },
        json = dataset)
    responseData = responseData.json()  
    sns = responseData['analysis']['sns_index']
    pns = responseData['analysis']['pns_index']
    return sns, pns

connection(ssid, pssw)
while True:
    intervals = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812, 812, 756, 820, 812, 800]
    sns, pns = request(intervals)
    oled.fill(0)
    oled.text('SNS: {:.2f}'.format(sns), 0, 0)
    oled.text('PNS: {:.2f}'.format(pns), 0, 10)
    oled.show()
