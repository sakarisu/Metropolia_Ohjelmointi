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
auto = Auto('ABC-123', 142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus on {Auto.nopeus:d} km/h.")
auto.kiihdyta(-200)
print(f"Teit hätäjarrutuksen, auton nopeus on nyt {Auto.nopeus:d} km/h")