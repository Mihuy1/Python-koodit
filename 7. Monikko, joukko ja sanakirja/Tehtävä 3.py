lentoasemat = {}

while True:

    valinta = input("1: Lisää uusi lentoasema, 2: hae lentoasemaa, 3: lopeta ohjelma: ")

    if valinta == "3":
        break

    if valinta == "1":
        icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
        lentoasemaNimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao_koodi] = lentoasemaNimi
        print("Lentoasema lisätty.")
    elif valinta == "2":
        icao_koodi = input("Lentoaseman ICAO-koodi: ")
        if icao_koodi in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao_koodi]}")
    else:
        print("Virheellinen valinta")


