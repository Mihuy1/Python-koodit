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


    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteri} ja huippunopeus: {self.huippunopeus}"


uusi_auto = Auto("ABC-123", 142)
print("Uusi auto:")
print(uusi_auto)

print("Kiihdytetään 30km/h")
uusi_auto.kiihdytä(30)

print("Kiihytetään 70km/h")
uusi_auto.kiihdytä(70)

print("Kiihdytetään 50km/h")
uusi_auto.kiihdytä(50)

print("Uusi nopeus: ", uusi_auto.nopeus, "km/h")

print("Hätäjarrutus!")
uusi_auto.kiihdytä(-200)
print("Uusi nopeus: ", uusi_auto.nopeus, "km/h")