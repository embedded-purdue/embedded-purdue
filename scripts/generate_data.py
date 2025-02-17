import pandas as pd
import json
import os
#This file is used to convert the data from the excel sheet to a json file 
#The json file is then used to populate the website
#Data is read from src/data/data.xlsx
#Resulting data is stored in src/data/sheet.json
file_path = os.path.join('src', 'data', 'data.xlsx')

df = pd.read_excel(file_path)

data = df.to_dict(orient='records')

json_file_path = os.path.join('src', 'data', 'sheet.json')

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=2)