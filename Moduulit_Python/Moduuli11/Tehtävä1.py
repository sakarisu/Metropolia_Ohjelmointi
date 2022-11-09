class Julkaisu:
    def __init__(self, nimi, sivumaara):
        self.nimi = nimi
        self.sivumaara = sivumaara
    def tulosta_tiedot(self):
        print(f"{self.nimi:s} \n{self.sivumaara:d} sivua")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi, sivumaara)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja:s}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja, sivumaara):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi, sivumaara)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja:s}")

julkaisut = []
julkaisut.append(Lehti('Aku Ankka', 'Aki Hyyppä', 36))
julkaisut.append(Kirja('Hytti nro 6', 'Rosa Liksom', 187))
for j in julkaisut:
    j.tulosta_tiedot()
