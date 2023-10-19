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

class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, kapasiteetti):
        self.kapasiteetti = kapasiteetti
        super().__init__(rekisteri, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensa):
        self.bensa = bensa
        super().__init__(rekisteri, huippunopeus)



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


sahko_auto = Sahkoauto("ABC-15", 180, 52.5)
auto = Polttomoottoriauto("ACD-123", 165, 32.3)
tunti_lkm = 3
tunti = 0

sahko_auto.nopeus = random.randint(60, sahko_auto.huippunopeus)
auto.nopeus = random.randint(60, auto.huippunopeus)

while tunti != tunti_lkm:
    sahko_auto.kulje(1)
    auto.kulje(1)
    tunti += 1

print(sahko_auto)
print(auto)


