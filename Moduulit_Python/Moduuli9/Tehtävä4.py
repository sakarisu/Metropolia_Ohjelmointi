import random
class Auto:#Edellisiin tehtäviin verrattuna tähän luokkarakenteeseen on tehty pieniä muutoksia
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
autot = []
reknum = 0
for i in range(10):
    reknum += 1
    autot.append(Auto(f"ABC-{reknum:d}", random.randint(100, 200), 0, 0))
kilpailu = True
while kilpailu:
    for i in autot:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje(1)
        if i.kilsat > 10000:
            kilpailu = False
for i in autot:
    print(f'{i}')