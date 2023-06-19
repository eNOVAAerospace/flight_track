from time import sleep
from library.user_define import *
from library.flight_scrapper import *
from library.format_json import *
from library.json_to_csv import *
from datetime import datetime


def get_data(n):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    namefile = f'{current_time}_flight'
    json_file = f'{namefile}.json'
    csv_file = f'tab_{namefile}.csv'
    with open(json_file, 'w') as file:
        pass
    with open(csv_file, 'w') as file:
        pass
    scrap_plane(json_file)
    format_json(json_file, json_file)
    json_to_csv(json_file, csv_file)
    print("all operations done")
    if n == 0:
        print('waiting an hour to proceed further.')
        sleep(3600)
        get_data(n)


n = get_user_choice()
get_data(n)
