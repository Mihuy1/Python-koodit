class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteri} ja huippunopeus: {self.huippunopeus}"


uusi_auto = Auto("ABC-123", 142)

print(uusi_auto)