import requests

# Configuration de l'API de FlightAware
username = 'YOUR_USERNAME'
apiKey = 'YOUR_API_KEY'

# Paramètres de requête
latitude = 47.6174
longitude = -52.7272
radius = 100  # en miles

# Construction de l'URL de l'API
url = f"https://flightxml.flightaware.com/json/FlightXML3/FlightInfoEx?howMany=10&lat={latitude}&lon={longitude}&radius={radius}"

# En-têtes de requête avec les informations d'authentification
headers = {
    'Authorization': f'Basic {username}:{apiKey}',
}

# Effectuer la requête GET à l'API
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Récupérer les données de la réponse en format JSON
    data = response.json()

    # Traiter les données
    flights = data['FlightInfoExResult']['flights']
    for flight in flights:
        flight_id = flight['ident']
        origin = flight['origin']
        destination = flight['destination']
        aircraft = flight['aircrafttype']

        # Afficher les informations du vol
        print("Flight ID:", flight_id)
        print("Origin:", origin)
        print("Destination:", destination)
        print("Aircraft:", aircraft)
        print("-----------------------------")
else:
    # Afficher un message d'erreur si la requête a échoué
    print("Erreur lors de la récupération des données de l'API")
