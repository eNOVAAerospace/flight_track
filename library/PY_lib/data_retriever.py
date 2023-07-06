from library.PY_lib.flight_scrapper import *
from library.PY_lib.format_json import *
from library.PY_lib.json_to_csv import *
from library.PY_lib.json_to_excel import *
from datetime import datetime
from time import sleep


def get_data(n, request_left, attente):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    namefile = f'{current_time}_flight'
    json_file = f'{namefile}.json'
    csv_file = f'tab_{namefile}.csv'
    excel_file = f'excel_{namefile}.xls'
    with open(json_file, 'w') as file:
        pass
    with open(csv_file, 'w') as file:
        pass
    with open(excel_file, 'w') as file:
        pass
    scrap_plane(json_file)
    format_json(json_file, json_file)
    json_to_csv(json_file, csv_file)
    json_to_excel(json_file, excel_file)
    print("all operations done")
    if n == 0 and request_left > 0:
        print(f'waiting {attente} seconds to proceed further, {request_left} request(s) left.')
        request_left = request_left - 1
        sleep(attente)
        get_data(n, request_left, attente)
