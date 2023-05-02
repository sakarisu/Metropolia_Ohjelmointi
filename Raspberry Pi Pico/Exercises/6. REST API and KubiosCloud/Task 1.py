import network
import urequests


ssid = 'KME670Group8'
pssw = 'or2i2hA00HVJsa1xMiIs'

def connect(ssid, pssw):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting...")
        wlan.connect(ssid, pssw)
        while not wlan.isconnected():
            pass
    print("Connected!")
    print("IP address:", wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

ip = connect(ssid, pssw)

url = 'http://' + ip + ':8000'
response = urequests.get(url)
print('Response:', response.text)
