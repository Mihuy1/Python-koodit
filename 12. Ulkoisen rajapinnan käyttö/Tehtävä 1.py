import json
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()
print(json_vastaus["value"])