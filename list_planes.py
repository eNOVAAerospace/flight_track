from library.reading_file import *
from library.coordinates import *

filename = input('Entrez le nom du fichier CSV entier (incluant l\'extension du fichier): ')
coord_path = 'coordinates.txt'
latitudes, longitudes = read_coordinates(coord_path)
data = read_csv(filename)
n = 0
new_filename = 'sorted_' + filename

with open(new_filename, 'w') as file :
    pass

print('calcul du nombre d\'avions dans une zone précise.')
for row in data:
    lat = row['lat']
    lng = row['lng']
    if float(latitudes[0]) <= float(lat) <= float(latitudes[1]) \
            or float(latitudes[0]) >= float(lat) >= float(latitudes[1]):
        n = n + 1
        print(f'plane number #{n}\tLat: {lat}\tLng: {lng}')
    # pas opti: print(f'#{n}\tLat:\t', row['lat'], '\tLng:\t', row['lng'])

print(latitudes)
print(longitudes)