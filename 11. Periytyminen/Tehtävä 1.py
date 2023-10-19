class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi



class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumaara}.")


class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi} ja päätoimittaja: {self.paatoimittaja}")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
print()
hytti_nro_6.tulosta_tiedot()
