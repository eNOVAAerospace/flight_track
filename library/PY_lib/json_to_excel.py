import csv
import json
import xlwt


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