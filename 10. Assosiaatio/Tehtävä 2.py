class Hissi():
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kerros):

        while self.kerros != kerros:
            if self.kerros < kerros:
                self.ylos()
            else:
                self.alas()

    def ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa: {self.kerros}")

    def alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa: {self.kerros}")


class Talo():
    def __init__(self, alin_kerros, ylin_kerros, hissit_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit_lkm = hissit_lkm
        self.hissit = []

        for hissi in range(hissit_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))


    def aja_hissiä(self, hissi_numero, kohdekerros):
        kohdehissi = self.hissit[hissi_numero - 1]

        kohdehissi.siirry_kerrokseen(kohdekerros)


t = Talo(1, 20, 10)
t.aja_hissiä(5, 20)
t.aja_hissiä(5, 5)
