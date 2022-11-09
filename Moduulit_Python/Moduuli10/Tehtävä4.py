import random
class Auto:
    def __init__(self, rekkari, huiput, nopeus, kilsat):
        self.rekkari = rekkari
        self.huiput = huiput
        self.nopeus = nopeus
        self.kilsat = kilsat
    def kiihdyta(self, kmh):
        self.nopeus += kmh
        if self.nopeus <= 0:
            self.nopeus = 0
        if self.nopeus >= self.huiput:
            self.nopeus = self.huiput
    def kulje(self, h):
        self.kilsat += self.nopeus*h
    def __str__(self):
        return f'{self.rekkari} \n {self.huiput} \n {self.nopeus} \n {self.kilsat}'
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for i in autot:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)
    def tulosta_tilanne(self):
        for i in autot:
            print(i)
    def kilpailu_ohi(self):
        for i in autot:
            if i.kilsat <= self.pituus:
                return True
autot = []
reknum = 0
for i in range(10):
    reknum += 1
    autot.append(Auto(f"ABC-{reknum:d}", random.randint(100, 200), 0, 0))
kisa = Kilpailu('Suuri romuralli', 8000, autot)
kilpailuOhi = False
tunteja = 10
while not kilpailuOhi:
    kisa.tunti_kuluu()
    if kisa.kilpailu_ohi():
        kisa.tulosta_tilanne()
        kilpailuOhi = True
    if tunteja == 10:
        tunteja = 0
        kisa.tulosta_tilanne()
    tunteja += 1