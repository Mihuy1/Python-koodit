import json, requests

API = "05e56269e9c5575ff8e56b4e16913e7e"

kaupunki_input = input("Kaupunki: ")


pyyntö_kaupunki = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki_input}&limit=5&appid={API}"

try:

    vastaus_kaupunki = requests.get(pyyntö_kaupunki)
    json_vastaus_kaupunki = vastaus_kaupunki.json()

    kaupunki = json_vastaus_kaupunki[0]["name"]
    lat = json_vastaus_kaupunki[0]["lat"]
    lon = json_vastaus_kaupunki[0]["lon"]

    pyyntö_sää = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric"

    vastaus_sää = requests.get(pyyntö_sää)
    json_vastaus_sää = vastaus_sää.json()

    lämpötila = json_vastaus_sää["main"]["temp"]
    kuvaus = json_vastaus_sää["weather"][0]["description"]

    print(f"Currently in {kaupunki} it is {round(lämpötila)} degrees Celsius. Weather description: {kuvaus}.")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")

