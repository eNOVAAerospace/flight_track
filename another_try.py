import requests
import csv

api_key = "c78bbb29-56b2-4347-9d89-fd3e72238896"
url = f"https://airlabs.co/api/v9/routes?api_key={api_key}"

# Effectuer une requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Récupérer les données de la réponse en format JSON
    data = response.json()

    # Définir les noms des champs pour le fichier CSV
    fieldnames = [
        "airline_iata",
        "airline_icao",
        "flight_number",
        "flight_iata",
        "flight_icao",
        "cs_airline_iata",
        "cs_flight_iata",
        "cs_flight_number",
        "dep_iata",
        "dep_icao",
        "dep_time",
        "dep_time_utc",
        "dep_terminals",
        "arr_iata",
        "arr_icao",
        "arr_time",
        "arr_time_utc",
        "arr_terminals",
        "duration",
        "days",
        "aircraft_icao",
        "updated"
    ]

    # Ouvrir le fichier CSV en mode écriture
    with open("routes.csv", mode="w", newline="") as file:
        # Créer un objet writer pour écrire dans le fichier CSV
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Écrire les en-têtes dans le fichier CSV
        writer.writeheader()
        # Écrire chaque ligne de données dans le fichier CSV
        for route in data:
            writer.writerow(route)

    print("Les données ont été écrites dans le fichier routes.csv.")
else:
    # Afficher un message d'erreur si la requête a échoué
    print("Erreur lors de la récupération des données de l'API")