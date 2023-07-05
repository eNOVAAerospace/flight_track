from library.reading_file import *
from library.coordinates import *
from library.read_excel import *
from library.calculate_distance import *

# filename = input('Entrez le nom du fichier CSV entier (incluant l\'extension du fichier): ')
# coord_path = 'coordinates.txt'
# latitudes, longitudes = read_coordinates(coord_path)
# data = read_csv(filename)
# n = 0
# new_filename = 'sorted_' + filename
# with open(new_filename, 'w', newline='') as file:
#     writer = csv.writer(file)
#     param_names = list(data[0].keys())
#     writer.writerow(param_names)
# print('calcul du nombre d\'avions dans une zone précise.') for row in data: lat = row['lat'] lng = row['lng'] if
# float(latitudes[0]) <= float(lat) <= float(latitudes[1]) and float(longitudes[0]) <= float(lng) <= float(
# longitudes[1]) or float(latitudes[0]) >= float(lat) >= float(latitudes[1]) and float(longitudes[0]) >= \ float(lng)
# >= float(longitudes[1]): n = n + 1 row_values = list(row.values()) writer.writerow(row_values)
#
#             print(f'plane number #{n}\tLat: {lat}\tLng: {lng}')
# print(f'Tout a été enregistré dans le fichier : {new_filename}')

filename = input('Entrez le nom du fichier XLS entier (incluant l\'extension du fichier): ')
coord_path = 'coordinates.txt'
latitudes, longitudes = read_coordinates(coord_path)
data = pd.read_excel(filename)
data = pd.DataFrame(data)
new_filename = 'sorted_' + filename + 'x'

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