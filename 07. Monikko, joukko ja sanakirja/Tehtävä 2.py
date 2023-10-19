nimet = set()

while True:

    nimi = input("Anna nimi: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimet")
        continue

    nimet.add(nimi)
    print("Uusi nimi")


for n in nimet:
    print(n)
