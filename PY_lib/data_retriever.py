from datetime import datetime
from time import sleep
import os
import pandas as pd
import requests
import csv
import json
import xlwt

from PY_lib.pyMath import *

def get_user_choice():
    """GUI (Graphic User Interface) limitée permettant l'automatisation de requetes API

    Returns:
        int: choix utilisateurs
    """
    while True:
        print('Voulez-vous automatiser la récupération de données ?')
        print('Oui : 0')
        print('Non : 1')
        see = input('Votre choix : ')
        if see == '1':
            return int(see), 0, 0
        print("Entrez le nombre de requetes que vous voulez completer au total.")
        nb_requests = input('Nombre de requetes : ')
        print('Entrez le temps d\'attente entre chaque requete. Entrez le temps en secondes. Exemple : pour 1 heure, '
              'entrez 3600. ')
        time_request = input('Temps : ')
        if see == '0' and '0' < nb_requests and time_request > '0':
            return int(see), int(nb_requests), int(time_request)
        else:
            print('Choix invalide.')


def user_preferences():
    """GUI (Graphic User Interface) limitée pour filtrer les données d'une zone

    Returns:
        int: choix utilisateurs
    """
    valid = 0
    zone_size = 0
    while True:
        valid = 0
        filename = input('Entrez le nom du fichier XLS entier (incluant l\'extension du fichier): ')
        if not os.path.exists(filename):
            print("Choix invalide.")
            valid = 1
        ros = input("Choisissez le type de filtrage :\nQuadrilatère : 1\nCirculaire : 2\nVotre choix : ")
        if ros == '1':
            return filename, 0, int(ros)
        elif ros == '2':
            zone_size = input('Entrez le rayon de la zone que vous vous filtrer : ')
            if zone_size <= '0':
                print("Choix invalide.")
                valid = 1
        else:
            print("Choix invalide")
            valid = 1
        if valid == 1:
            continue
        else:
            return filename, int(zone_size), int(ros)

def read_coordinates(file_path):
    latitudes = []
    longitudes = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('lat'):
                lat_values = line.split(':')[1].strip().split()
                latitudes.extend(lat_values)
            elif line.startswith('lng'):
                lng_values = line.split(':')[1].strip().split()
                longitudes.extend(lng_values)
    return latitudes, longitudes

def scrap_plane(input_json):
    api_key = '361444b0-bbd6-4da0-a1ce-85a76197bd4f'
    url = f"https://airlabs.co/api/v9/flights?lat=0&lon=0&distance=10&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(input_json, mode="w") as file:
            json.dump(data, file)
        print(f'Data written in {input_json}')
    else:
        print("Error when retrieving API data")


def get_data(n, request_left, attente):
    """Automatise les requetes API

    Args:
        n (int): nombre total de requetes
        request_left (int): requetes restantes
        attente (int): délai entre 2 requetes en secondes
    """
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    file_name = f'{current_time}_flight'
    json_file = f'{os.path.join("Data","tempo.json")}'
    # csv_file = f'tab_{namefile}.csv'
    excel_file = f'{os.path.join("Data", "API_extract",file_name)}.xlsx'
    with open(json_file, 'w') as file:
        pass
    # with open(csv_file, 'w') as file:
    #     pass
    with open(excel_file, 'w') as file:
        pass
    scrap_plane(json_file)
    format_json(json_file, json_file)
    # json_to_csv(json_file, csv_file)
    json_to_excel(json_file, excel_file)

    df=pd.read_excel(excel_file)
    df['Date']=current_time
    df.to_excel(excel_file, index=False)

    # os.remove(json_file)

    print(f'{file_name} has been saved to {os.path.join("Data", "API_extract")}')

    if n == 0 and request_left > 0:
        print(f'waiting {attente} seconds to proceed further, {request_left} request(s) left.')
        request_left = request_left - 1
        sleep(attente)
        get_data(n, request_left, attente)


def onefiledata(filename, taille_zone, choice, r_latitudes, r_longitude, s_latitude, s_longitude):
    # print(filename)
    data = pd.read_excel(filename)
    data = pd.DataFrame(data)

    if choice == 1:
        t_lat = s_latitude
        t_lng = s_longitude
        # filtered_data = []
        for index, row in data.iterrows():
            lat = row['lat']
            lng = row['lng']
            if sort_elements(t_lat[0], t_lat[1], t_lat[2], t_lat[3], lat, t_lng[0], t_lng[1], t_lng[2], t_lng[3], lng) == 0:
                data.loc[index,'distance'] = True
        filtered_data=data.where(data['distance']==True)

    if choice == 2:
        for index, row in data.iterrows():
            lat = row['lat']
            lng = row['lng']
            for ref_lat, ref_lng in zip(r_latitudes, r_longitude):
                data.loc[index,'distance'] = calculate_distance(lat, lng, float(ref_lat), float(ref_lng))
        filtered_data=data.where(data['distance']<=taille_zone)
    # display(filtered_data.dropna())
    return filtered_data.dropna()

def format_json(file_in, file_out):
    with open(file_in, 'r') as f_in:
        data = json.load(f_in)
    formatted_data = json.dumps(data, indent=4)
    with open(file_out, 'w') as f_out:
        f_out.write(formatted_data)

def json_to_csv(file_in, file_out):
    with open(file_in) as file:
        data = json.load(file)

    response_data = data['response']
    param_names = [
        'hex', 'reg_number', 'flag', 'lat', 'lng', 'alt', 'dir', 'speed',
        'v_speed', 'squawk', 'flight_number', 'flight_icao', 'flight_iata',
        'dep_icao', 'dep_iata', 'arr_icao', 'arr_iata', 'airline_icao',
        'airline_iata', 'aircraft_icao', 'updated', 'status'
    ]

    with open(file_out, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(param_names)

        for response_item in response_data:
            row = []
            for param_name in param_names:
                param_value = response_item.get(param_name, '')
                row.append(param_value)
            writer.writerow(row)

    print(f'Data converted to {file_out}')

def json_to_excel(file_in, file_out):
    with open(file_in) as file:
        data = json.load(file)
    response_data = data['response']
    param_names = [
        'hex', 'reg_number', 'flag', 'lat', 'lng', 'alt', 'dir', 'speed',
        'v_speed', 'squawk', 'flight_number', 'flight_icao', 'flight_iata',
        'dep_icao', 'dep_iata', 'arr_icao', 'arr_iata', 'airline_icao',
        'airline_iata', 'aircraft_icao', 'updated', 'status'
    ]
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet 1')
    for col_index, param_name in enumerate(param_names):
        sheet.write(0, col_index, param_name)
    for row_index, response_item in enumerate(response_data, start=1):
        for col_index, param_name in enumerate(param_names):
            param_value = response_item.get(param_name, '')
            sheet.write(row_index, col_index, param_value)
    workbook.save(file_out)
    print(f'Data converted to {file_out}')

def read_excel(file_path):
    data = pd.read_excel(file_path)
    return data.to_dict('records')

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
    return data
