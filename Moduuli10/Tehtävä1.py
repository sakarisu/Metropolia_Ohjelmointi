class Hissi:
    kerros = 1
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros:d}")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros:d}")
    def siirry_kerrokseen(self, mihin):
        self.mihin = mihin
        print(f"Hissi on kerroksessa {self.kerros:d}")
        if self.kerros <= mihin:
            while self.kerros <= mihin:
                self.kerros_ylos()
                if self.kerros == mihin:
                    break
        elif self.kerros >= mihin:
            while self.kerros >= mihin:
                self.kerros_alas()
                if self.kerros == mihin:
                    break
h = Hissi(5, 1)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
