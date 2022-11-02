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
class Sahko(Auto):
    def __init__(self, rekkari, huiput, kapasiteetti, nopeus, kilsat):
        self.kapasiteetti = kapasiteetti
        super().__init__(rekkari, huiput, nopeus, kilsat)
    def __str__(self):
        return f'Auto {self.rekkari} kulki {self.nopeus}km/h yhteensä {self.kilsat}km \n Akun kapasiteetti on {self.kapasiteetti}kWh \n'
class Polttomoottori(Auto):
    def __init__(self, rekkari, huiput, tankki, nopeus, kilsat):
        self.tankki = tankki
        super().__init__(rekkari, huiput, nopeus, kilsat)
    def __str__(self):
        return f'Auto {self.rekkari} kulki {self.nopeus}km/h yhteensä {self.kilsat}km \n Tankkiin mahtuu {self.tankki}litraa \n'
autot = []
autot.append(Sahko('ABC-15', 180, 52.5, 0, 0))
autot.append(Polttomoottori('ACD-123', 165, 32.3, 0, 0))
for a in autot:
    a.kiihdyta(random.randint(0, 200))
    a.kulje(3)
    print(a)
