import random
class Hissi:
    def __init__(self, ylin, alin, kerros):
        self.ylin = ylin
        self.alin = alin
        self.kerros = kerros
    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros:d}")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros:d}")
    def siirry_kerrokseen(self, mihin):
        self.mihin = mihin
        if self.kerros <= self.mihin:
            while self.kerros <= self.mihin:
                self.kerros_ylos(self)
                if self.kerros == self.mihin:
                    break
        elif self.kerros >= self.mihin:
            while self.kerros >= self.mihin:
                self.kerros_alas(self)
                if self.kerros == self.mihin:
                    break
class Talo:
    def __init__(self, ylin, alin, hissit):
        self.ylin = ylin
        self.alin = alin
        self.hissit = []
        for i in range(hissit):
            self.hissit.append(Hissi(5, 1, 1))
    def aja_hissia(self, numero, kohde):
        self.numero = numero
        self.kohde = kohde
        Hissi.siirry_kerrokseen(Hissi, kohde)
talo = Talo(5, 1, 3)
setattr(Hissi, 'kerros', 1)
talo.aja_hissia(random.choice(talo.hissit), int(input('Valitse kerros 1-5 ')))