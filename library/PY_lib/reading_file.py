import csv


def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
    return data
