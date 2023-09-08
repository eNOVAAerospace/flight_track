from library.PY_lib.coordinates import *
from library.PY_lib.read_excel import *
from library.PY_lib.calculate_distance import *
from library.PY_lib.user_define import *
from library.quad_filter import *
import os


round_path = 'D:\Programmes\E.nova\python\PyEnova\flight_track\round_coordinates.txt'
square_path = 'square_coordinates.txt'
filtered_data = []

folder, taille_zone, choice = user_preferences()
r_latitudes, r_longitude = read_coordinates(round_path)
s_latitude, s_longitude = read_coordinates(square_path)

filename = os.listdir(folder)
for i in range(len(filename)):
    filtered_data=onefiledata(filename[i],taille_zone, choice, r_latitudes, r_longitude, s_latitude, s_longitude)
    df[i]=pd.DataFrame(filtered_data)


filtered_df = pd.concat([df[i]])
filtered_df.to_excel(new_filename, index=False)

print(f"Tout a été enregistré dans le fichier : {new_filename}")



def onefiledata(filename, r_latitudes, r_longitude, s_latitude, s_longitude):
    data = pd.read_excel(filename)
    data = pd.DataFrame(data)
    new_filename = 'sorted_' + filename + 'x'

    if choice == 1:
        new_filename = 'square_' + new_filename
        t_lat = s_latitude
        t_lng = s_longitude
        filtered_data = []
        for index, row in data.iterrows():
            lat = row['lat']
            lng = row['lng']
            if sort_elements(t_lat[0], t_lat[1], t_lat[2], t_lat[3], lat, t_lng[0], t_lng[1], t_lng[2], t_lng[3], lng) == 0:
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
    return filtered_data