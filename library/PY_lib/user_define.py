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
            print('Choix invalide. Veuillez entrer 0 ou 1.')


def user_preferences():
    valid = 0
    while True:
        filename = input('Entrez le nom du fichier XLS entier (incluant l\'extension du fichier): ')
        if not os.path.exists(filename):
            print("Choix invalide.")
            valid = 1
        if valid == 1:
            continue
        else:
            return filename
