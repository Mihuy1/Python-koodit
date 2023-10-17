class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

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
        return f"Rekisteritunnus: {self.rekisteri} ja huippunopeus: {self.huippunopeus}"


uusi_auto = Auto("ABC-123", 142)
print("Uusi auto:")
print(uusi_auto)

uusi_auto.kulje(1.5)
print("Kuljettu matka:", uusi_auto.matka)