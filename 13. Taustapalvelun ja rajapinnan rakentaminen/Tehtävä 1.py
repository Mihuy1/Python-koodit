from flask import Flask, Response
import json
import mysql.connector


conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='123',
    autocommit=True
)


def airport_information(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchall()
    return result


app = Flask(__name__)


@app.route('/kenttä/<icao>')
def kenttä(icao):
    try:
        airport = airport_information(icao)
        name = airport[0]['name']
        municipality = airport[0]['municipality']
        tilakoodi = 200

        vastaus = {
            "ICAO": icao,
            "Name": name,
            "Municipality": municipality
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virhe"
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen paatypiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
