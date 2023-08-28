import geopy.distance
import mysql.connector
from geopy.distance import geodesic


yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='123',
    autocommit=True
)

def haeLentokenttienKoordinaatit(icao_koodi):
    kursori = yhteys.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao_koodi,))
    return kursori.fetchall()


icao_koodi1 = input("Anna ensimmäisen lentokentän ICAO-koodin: ")
icao_koodi2 = input("Anna toisen lentokentän ICAO-koodi: ")

koordinaatit = haeLentokenttienKoordinaatit(icao_koodi1)
koordinaatit2 = haeLentokenttienKoordinaatit(icao_koodi2)

etaisyys = geodesic(koordinaatit, koordinaatit2).kilometers

print(etaisyys)
