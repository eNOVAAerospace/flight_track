import csv
import json


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
