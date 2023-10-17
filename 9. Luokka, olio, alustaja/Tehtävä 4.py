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

autot = []

for i in range(10):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i+1}", huippunopeus)
    autot.append(auto)

while True:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

    if any(auto.matka >= 10000 for auto in autot):
        break

for auto in autot:
    print(auto)