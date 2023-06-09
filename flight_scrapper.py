import requests
import json

api_key = 'c78bbb29-56b2-4347-9d89-fd3e72238896'
url = f"https://airlabs.co/api/v9/flights?lat=0&lon=0&distance=10&api_key={api_key}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    with open("i.json", mode="w") as file:
        json.dump(data, file)
    print("Les données ont été écrites dans le fichier routes.json.")
else:
    print("Erreur lors de la récupération des données de l'API")
