import math


def PizzaHinta(halkaisija, hinta):
    alue = math.pi * (halkaisija / 2) ** 2
    yksikkohinta = hinta / alue

    return yksikkohinta


halkaisija1 = int(input("Anna pizzan halkaisija: "))
hinta1 = int(input("Anna pizzan hinta: "))

halkaisija2 = int(input("Anna pizzan halkaisija: "))
hinta2 = int(input("Anna pizzan hinta: "))

pizzaHinta1 = PizzaHinta(halkaisija1, hinta1)
pizzaHinta2 = PizzaHinta(halkaisija2, hinta2)

if pizzaHinta1 < pizzaHinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
elif pizzaHinta2  < pizzaHinta1:
    print("Toinen pizza antaa paremman vastineen rahalle")
else:
    print("Pizzat ovat saman hintaisia.")