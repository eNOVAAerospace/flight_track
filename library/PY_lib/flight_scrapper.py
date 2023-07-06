import requests
import json


def scrap_plane(input_json):
    api_key = 'c78bbb29-56b2-4347-9d89-fd3e72238896'
    url = f"https://airlabs.co/api/v9/flights?lat=0&lon=0&distance=10&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(input_json, mode="w") as file:
            json.dump(data, file)
        print(f'Data written in {input_json}')
    else:
        print("Error when retrieving API data")
