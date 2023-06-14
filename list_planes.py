from library.reading_file import *
from library.coordinates import *

filename = input('Entrez le nom du fichier CSV entier (incluant l\'extension du fichier): ')
coord_path = 'coordinates.txt'

latitudes, longitudes = read_coordinates(coord_path)

data = read_csv(filename)
n = 0
for row in data:
    print('calcul du nombre d\'avions dans une zone précise')
    n = n + 1
    print(f'#{n}\tLat:\t', row['lat'], '\tLng:\t', row['lng'])



print(latitudes)
print(longitudes)