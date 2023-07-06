import row as row

from library.PY_lib.coordinates import *
from library.PY_lib.read_excel import *
from library.PY_lib.calculate_distance import *
# from library.PY_lib.reading_file import read_csv
from library.PY_lib.user_define import *

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
# print('calcul du nombre d\'avions dans une zone précise.')
# for row in data:
#     lat = row['lat']
#     lng = row['lng']
#     if float(latitudes[0]) <= float(lat) <= float(latitudes[1]) and float(longitudes[0]) <= float(lng) <= float(
#             longitudes[1]) or float(latitudes[0]) >= float(lat) >= float(latitudes[1]) and float(
#             longitudes[0]) >= float(lng) >= float(longitudes[1]):
#         n = n + 1
#         row_values = list(row.values())
#         writer.writerow(row_values)
#
# print(f'plane number #{n}\tLat: {latitudes}\tLng: {longitudes}')
# print(f'Tout a été enregistré dans le fichier : {new_filename}')

coord_path = 'coordinates.txt'
filtered_data = []

filename, taille_zone, choice = user_preferences()
latitudes, longitudes = read_coordinates(coord_path)
data = pd.read_excel(filename)
data = pd.DataFrame(data)
new_filename = 'sorted_' + filename + 'x'

# if choice == 1:
#     for row in data:
#         lat = row['lat']
#         lng = row['lng']
#         if float(latitudes[0]) <= float(lat) <= float(latitudes[1]) and float(longitudes[0]) <= float(lng) <= float(
#                 longitudes[1]) or float(latitudes[0]) >= float(lat) >= float(latitudes[1]) and float(
#             longitudes[0]) >= float(lng) >= float(longitudes[1]):
#             n = n + 1
#             row_values = list(row.values())
#             writer.writerow(row_values)

for index, row in data.iterrows():
    lat = row['lat']
    lng = row['lng']
    for ref_lat, ref_lng in zip(latitudes, longitudes):
        distance = calculate_distance(lat, lng, float(ref_lat), float(ref_lng))
        if distance <= taille_zone:
            filtered_data.append(row)
            break

filtered_df = pd.DataFrame(filtered_data)
filtered_df.to_excel(new_filename, index=False)

print(f"Tout a été enregistré dans le fichier : {new_filename}")
