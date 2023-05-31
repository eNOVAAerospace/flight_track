import requests
import json

api_key = "c78bbb29-56b2-4347-9d89-fd3e72238896"
url = f"https://airlabs.co/api/v9/routes?api_key={api_key}"

# Effectuer une requête GET à l'API
response = requests.get(url)
# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Récupérer les données de la réponse en format JSON
    data = response.json()
    # Enregistrer les données dans un fichier JSON
    with open("routes.json", mode="w") as file:
        json.dump(data, file)
    print("Les données ont été écrites dans le fichier routes.json.")
else:
    # Afficher un message d'erreur si la requête a échoué
    print("Erreur lors de la récupération des données de l'API")
