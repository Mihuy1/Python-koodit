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


h = Hissi(1, 10)

h.siirry_kerrokseen(10)
h.siirry_kerrokseen(1)

