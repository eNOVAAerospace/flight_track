import json


def format_json(file_in, file_out):
    with open(file_in, 'r') as f_in:
        data = json.load(f_in)

    formatted_data = json.dumps(data, indent=4)

    with open(file_out, 'w') as f_out:
        f_out.write(formatted_data)

    print(f"Le fichier JSON a été formaté avec succès. Le résultat a été enregistré dans '{file_out}'.")


file_in = 'al_test.json'  # Fichier JSON d'entrée
file_out = 'al_test_format.json'  # Fichier JSON formaté en sortie

format_json(file_in, file_out)
