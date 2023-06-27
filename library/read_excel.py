import pandas as pd
import xlsxwriter


def read_excel(file_path):
    data = pd.read_excel(file_path)
    return data.to_dict('records')
