import pandas as pd

# Sample data. This is strictly for testing. Data can be put into data.xlsx manually as needed.

data = {
    'Name': ['Alice Johnson', 'Bob Smith', 'Carol White', 'Dave Brown', 'Eve Black', 'Frank Green'],
    'Role': ['Exec', 'Exec', 'PM', 'PM', 'Active Member', 'Active Member'],
    'Image': ['alice.jpg', 'bob.jpg', 'carol.jpg', 'dave.jpg', 'eve.jpg', 'frank.jpg'],
    'MajorYear': ['CS Senior', 'EE Junior', 'ME Sophomore', 'CE Freshman', 'CS Senior', 'EE Junior'],
    'LinkedIn': [
        'https://linkedin.com/in/alicejohnson',
        'https://linkedin.com/in/bobsmith',
        'https://linkedin.com/in/carolwhite',
        'https://linkedin.com/in/davebrown',
        'https://linkedin.com/in/eveblack',
        'https://linkedin.com/in/frankgreen'
    ]
}

df = pd.DataFrame(data)

file_path = 'src/data/data.xlsx'

df.to_excel(file_path, index=False)

print(f"Data has been written to {file_path}")