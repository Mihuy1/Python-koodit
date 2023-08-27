import mysql.connector

# Yhdistetään tietokantaan
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='123',
    autocommit=True
)


def haeLentokenttaTiedot(maakoodi):
    kursori = yhteys.cursor()
    sql = "SELECT type FROM airport WHERE iso_country = %s"
    kursori.execute(sql, (maakoodi,))
    return kursori.fetchall()

def jarjestaLentokentat(lentokentta_tiedot):
    heliport_lkm = 0
    pieni_lentokentta_lkm = 0
    keski_lentokentta_lkm = 0
    iso_lentokentta_lkm = 0
    suljettu_lkm = 0

    for rivi in lentokentta_tiedot:
        lentokentan_tyyppi = rivi[0]
        if lentokentan_tyyppi == "heliport":
            heliport_lkm += 1
        elif lentokentan_tyyppi == "small_airport":
            pieni_lentokentta_lkm += 1
        elif lentokentan_tyyppi == "medium_airport":
            keski_lentokentta_lkm += 1
        elif lentokentan_tyyppi == "large_airport":
            iso_lentokentta_lkm += 1
        else:
            suljettu_lkm += 1

    print("Lentokenttien lukumäärät:")
    print(f"Helikopteri kenttiä: {heliport_lkm}")
    print(f"Pieniä lentokenttiä: {pieni_lentokentta_lkm}")
    print(f"Keskikokoisia lentokenttiä: {keski_lentokentta_lkm}")
    print(f"Isoja lentokenttiä: {iso_lentokentta_lkm}")
    print(f"Suljettuja lentokenttiä: {suljettu_lkm}")


maakoodi = input("Anna maakoodi: ")
lentokentta_tiedot = haeLentokenttaTiedot(maakoodi)
jarjestaLentokentat(lentokentta_tiedot)

