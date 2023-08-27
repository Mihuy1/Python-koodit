import mysql.connector

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='123',
         autocommit=True
         )


def haeLentokenttaTietokanta(ident):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident='" + ident + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(f"Lentokentän nimi on {rivi[1]} ja paikkakunta on {rivi[2]}")
    return



icao = input("Anna lentokentän ICAO-koodi: ")
haeLentokenttaTietokanta(icao)


