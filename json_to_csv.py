import csv
import json

with open('i.json') as file:
    data = json.load(file)

response_data = data['response']

parameters = []
for response_item in response_data:
    parameters.append(list(response_item.values()))

param_names = list(response_data[0].keys())
parameters.insert(0, param_names)
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(parameters)
