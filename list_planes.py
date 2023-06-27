from library.reading_file import *
from library.coordinates import *
from library.read_excel import *


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
data = read_excel(filename)
n = 0
new_filename = 'sorted_' + filename

writer = pd.ExcelWriter(new_filename, engine='xlsxwriter')
df = pd.DataFrame(data)

for index, row in df.iterrows():
    lat = row['lat']
    lng = row['lng']
    if float(latitudes[0]) <= float(lat) <= float(latitudes[1]) and float(longitudes[0]) <= float(lng) <= float(
            longitudes[1]) or float(latitudes[0]) >= float(lat) >= float(latitudes[1]) and float(longitudes[0]) >= \
            float(lng) >= float(longitudes[1]):
        n += 1
    else:
        df.drop(index, inplace=True)
df.to_excel(writer, index=False)
writer.save()

print(f'Tout a été enregistré dans le fichier : {new_filename}')
