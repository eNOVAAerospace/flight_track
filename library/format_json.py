import json


def format_json(file_in, file_out):
    with open(file_in, 'r') as f_in:
        data = json.load(f_in)
    formatted_data = json.dumps(data, indent=4)
    with open(file_out, 'w') as f_out:
        f_out.write(formatted_data)
