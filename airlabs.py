import requests

api_key = "c78bbb29-56b2-4347-9d89-fd3e72238896"
url = f"https://airlabs.co/api/v9/routes?api_key={api_key}"

# Effectuer une requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Récupérer les données de la réponse en format JSON
    data = response.json()

    # Traiter les données
    for route in data:
        airline_iata = route.get('airline_iata', '')
        airline_icao = route.get('airline_icao', '')
        flight_number = route.get('flight_number', '')
        flight_iata = route.get('flight_iata', '')
        flight_icao = route.get('flight_icao', '')
        dep_iata = route.get('dep_iata', '')
        dep_icao = route.get('dep_icao', '')
        dep_time = route.get('dep_time', '')
        dep_time_utc = route.get('dep_time_utc', '')
        arr_iata = route.get('arr_iata', '')
        arr_icao = route.get('arr_icao', '')
        arr_time = route.get('arr_time', '')
        arr_time_utc = route.get('arr_time_utc', '')
        duration = route.get('duration', '')
        aircraft_icao = route.get('aircraft_icao', '')

        # Afficher les informations des routes
        print("Airline:", airline_iata)
        print("Flight Number:", flight_number)
        print("Departure:", dep_iata)
        print("Departure Time:", dep_time)
        print("Arrival:", arr_iata)
        print("Arrival Time:", arr_time)
        print("Duration:", duration, "minutes")
        print("-----------------------------")
else:
    # Afficher un message d'erreur si la requête a échoué
    print("Erreur lors de la récupération des données de l'API")
