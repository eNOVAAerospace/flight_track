import pandas as pd
import math


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


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


filename = input('Entrez le nom du fichier XLS entier (incluant l\'extension du fichier): ')
coord_path = 'coordinates.txt'
latitudes, longitudes = read_coordinates(coord_path)
data = pd.read_excel(filename)
data = pd.DataFrame(data)
new_filename = 'sorted_' + filename

filtered_data = []
for index, row in data.iterrows():
    lat = row['lat']
    lng = row['lng']
    for ref_lat, ref_lng in zip(latitudes, longitudes):
        distance = calculate_distance(lat, lng, float(ref_lat), float(ref_lng))
        if distance <= 100:  # Filtrer les avions dans un rayon de 100 km
            filtered_data.append(row)
            break

filtered_df = pd.DataFrame(filtered_data)
filtered_df.to_excel(new_filename, index=False)

print(f"Tout a été enregistré dans le fichier : {new_filename}")
