def get_user_choice():
    while True:
        print('Voulez-vous automatiser la récupération de données ? Les requêtes seront faites toutes les heures.')
        print('Oui : 0')
        print('Non : 1')
        see = input('Votre choix : ')
        if see == '0' or see == '1':
            return int(see)
        else:
            print('Choix invalide. Veuillez entrer 0 ou 1.')