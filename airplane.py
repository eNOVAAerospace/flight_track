import requests


def get_aircraft_data(latitude, longitude, radius):
    url = f"https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat={latitude}&lng={longitude}&fDstL={radius}"
    response = requests.get(url)
    data = response.json()
    return data['acList']


def main():
    # Coordonnées de Terre-Neuve-et-Labrador
    latitude = 47.5362
    longitude = -52.7126
    radius = 100  # Rayon en miles

    aircraft_data = get_aircraft_data(latitude, longitude, radius)

    for aircraft in aircraft_data:
        # Récupérer les informations souhaitées
        lat = aircraft['Lat']
        lon = aircraft['Long']
        cap = aircraft['Trak']
        sqwak = aircraft['Sqk']
        heure_passage = aircraft['PosTime']

        # Afficher les informations
        print(f"Latitude: {lat}, Longitude: {lon}")
        print(f"Cap: {cap}, Sqwak: {sqwak}")
        print(f"Heure de passage: {heure_passage}")
        print("-----------------------------")


if __name__ == "__main__":
    main()
