import requests
import json

api_key = "c78bbb29-56b2-4347-9d89-fd3e72238896"
url = "https://airlabs.co/api/v9/flights"
params = {
    "_view": "array",
    "_fields": "hex,flag,lat,lng,dir,alt",
    "api_key": api_key
}

# Effectuer une requête GET à l'API avec les paramètres
response = requests.get(url, params=params)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Convertir la réponse en format JSON
    data = json.loads(response.text)

    # Traiter les données
    for flight in data:
        hex_code = flight.get('hex', '')
        flag = flight.get('flag', '')
        latitude = flight.get('lat', '')
        longitude = flight.get('lng', '')
        direction = flight.get('dir', '')
        altitude = flight.get('alt', '')

        # Afficher les informations des vols
        print("Hex Code:", hex_code)
        print("Flag:", flag)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Direction:", direction)
        print("Altitude:", altitude)
        print("-----------------------------")
else:
    # Afficher un message d'erreur si la requête a échoué
    print("Erreur lors de la récupération des données de l'API")
