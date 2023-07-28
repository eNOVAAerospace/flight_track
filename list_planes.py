from library.PY_lib.coordinates import *
from library.PY_lib.read_excel import *
from library.PY_lib.calculate_distance import *
from library.PY_lib.user_define import *


round_path = 'round_coordinates.txt'
square_path = 'square_coordinates.txt'
filtered_data = []

filename, taille_zone, choice = user_preferences()
r_latitudes, r_longitude = read_coordinates(round_path)
s_latitude, s_longitude = read_coordinates(square_path)
data = pd.read_excel(filename)
data = pd.DataFrame(data)
new_filename = 'sorted_' + filename + 'x'

if choice == 1:
    new_filename = 'square_' + new_filename
    s_latitudes = s_latitude
    s_longitudes = s_longitude
    filtered_data = []
    for index, row in data.iterrows():
        lat = row['lat']
        lng = row['lng']
        if float(s_latitudes[0]) <= lat <= float(s_latitudes[2]) and float(s_longitudes[0]) <= lng <= float(s_longitudes[2]) or float(s_latitudes[1]) <= lat <= float(s_latitudes[2]) and float(s_longitudes[1]) <= lng <= float(s_longitudes[2]) or float(s_latitudes[2]) <= lat <= float(s_latitudes[3]) and float(s_longitudes[2]) <= lng <= float(s_longitudes[3]) or float(s_latitudes[3]) <= lat <= float(s_latitudes[0]) and float(s_longitudes[3]) <= lng <= float(s_longitudes[0]):
            filtered_data.append(row)

if choice == 2:
    new_filename = 'round_' + new_filename
    for index, row in data.iterrows():
        lat = row['lat']
        lng = row['lng']
        for ref_lat, ref_lng in zip(r_latitudes, r_longitude):
            distance = calculate_distance(lat, lng, float(ref_lat), float(ref_lng))
            if distance <= taille_zone:
                filtered_data.append(row)
                break

filtered_df = pd.DataFrame(filtered_data)
filtered_df.to_excel(new_filename, index=False)

print(f"Tout a été enregistré dans le fichier : {new_filename}")

# if (latitudes[0] <= lat <= latitudes[2]) and (longitudes[0] <= lng <= longitudes[2]):
#      if (lat <= (latitudes[1] - latitudes[0]) * (lng - longitudes[0]) / (longitudes[1] - longitudes[0]) + latitudes[0]):
#          is_inside = True
#  if (latitudes[1] <= lat <= latitudes[3]) and (longitudes[1] >= lng >= longitudes[3]):
#      if (lat >= (latitudes[3] - latitudes[2]) * (lng - longitudes[2]) / (longitudes[3] - longitudes[2]) + latitudes[2]):
#          is_inside = True


# if float(s_latitudes[0]) <= lat <= float(s_latitudes[2]) and float(s_longitudes[0]) <= lng <= float(s_longitudes[2]) or \
#            float(s_latitudes[1]) <= lat <= float(s_latitudes[2]) and float(s_longitudes[1]) <= lng <= float(s_longitudes[2]) or \
#            float(s_latitudes[2]) <= lat <= float(s_latitudes[3]) and float(s_longitudes[2]) <= lng <= float(s_longitudes[3]) or \
#            float(s_latitudes[3]) <= lat <= float(s_latitudes[0]) and float(s_longitudes[3]) <= lng <= float(s_longitudes[0]):