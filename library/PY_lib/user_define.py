import os


def get_user_choice():
    while True:
        print('Voulez-vous automatiser la récupération de données ?')
        print('Oui : 0')
        print('Non : 1')
        see = input('Votre choix : ')
        if see == '1':
            return int(see), 0, 0
        print("Entrez le nombre de requetes que vous voulez completer au total.")
        nb_requests = input('Nombre de requetes : ')
        print('Entrez le temps d\'attente entre chaque requete. Entrez le temps en secondes. Exemple : pour 1 heure, '
              'entrez 3600. ')
        time_request = input('Temps : ')
        if see == '0' and '0' < nb_requests and time_request > '0':
            return int(see), int(nb_requests), int(time_request)
        else:
            print('Choix invalide.')


def user_preferences():
    valid = 0
    zone_size = 0
    while True:
        valid = 0
        filename = input('Entrez le nom du fichier XLS entier (incluant l\'extension du fichier): ')
        if not os.path.exists(filename):
            print("Choix invalide.")
            valid = 1
        ros = input("Choisissez le type de filtrage :\nQuadrilatère : 1\nCirculaire : 2\nVotre choix : ")
        if ros == '1':
            return filename, 0, int(ros)
        elif ros == '2':
            zone_size = input('Entrez le rayon de la zone que vous vous filtrer : ')
            if zone_size <= '0':
                print("Choix invalide.")
                valid = 1
        else:
            print("Choix invalide")
            valid = 1
        if valid == 1:
            continue
        else:
            return filename, int(zone_size), int(ros)
