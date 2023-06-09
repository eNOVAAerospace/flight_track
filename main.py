from flight_scrapper import *
from format_json import *
from json_to_csv import *
from datetime import datetime

if "__name__" == "__main__":
    json_file = f'{datetime.now()}_flights.json'
    csv_file = f'tab_{json_file}'
    scrap_plane(json_file)
    format_json(json_file, json_file)
    json_to_csv(json_file, csv_file)
    print("all operations done")

