import random
class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):

        if nopeuden_muutos > 0:
            self.nopeus += nopeuden_muutos

        elif nopeuden_muutos < 0:
            self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara

    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteri} ja huippunopeus: {self.huippunopeus} ja kuljettu matka: {self.matka}"

class Kilpailu:

    def __init__(self, nimi, pituus, auto_lista):
        self.nimi = nimi
        self.pituus = pituus
        self.auto_lista = auto_lista

    def tunti_kuluu(self):
        for auto in self.auto_lista:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.auto_lista:
            print(auto)

    def kilpailu_ohi(self):
        if any(auto.matka >= self.pituus for auto in self.auto_lista):
            return True
        else:
            return False



autot = []
tunnit = 0
valit = 10


for i in range(10):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i+1}", huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while True:

    kilpailu.tunti_kuluu()

    if tunnit != 0 and tunnit % valit == 0:
        kilpailu.tulosta_tilanne()
        print(f"Kilpailu on kulunut {tunnit}")

    if kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()
        print(f"Kilpailu on kulunut {tunnit}")
        break

    tunnit += 1
