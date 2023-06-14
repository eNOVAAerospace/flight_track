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
    # Afficher les valeurs des latitudes et longitudes
