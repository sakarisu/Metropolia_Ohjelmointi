class Auto:
    nopeus = 0
    kilsat = 0
    def __init__(self, rekkari, huiput):
        self.rekkari = rekkari
        self.huiput = huiput
    def kiihdyta(self, kmh):
        Auto.nopeus += kmh
        if Auto.nopeus <= 0:
            Auto.nopeus = 0
        if Auto.nopeus >= self.huiput:
            Auto.nopeus = self.huiput
    def kulje(self, h):
        Auto.kilsat += Auto.nopeus*h
auto = Auto('ABC-123', 142)
#Ohjelmaa ajettaessa ei erikseen kysytä kiihdytystä tai tuntimäärää(koska tehtävänannossa ei pyydetty erikseen)
#Ensin pitää laittaa kiihdytys ja sitten tunnit, jonka jälkeen ohjelma antaa ajetut kilometrit
auto.kiihdyta(int(input()))
auto.kulje(int(input()))
print(f"{Auto.kilsat:d}km.")