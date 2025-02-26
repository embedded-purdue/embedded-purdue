import pandas as pd
import json
import os
import re

# Define file paths
file_path = os.path.join('src', 'data', 'data2.xlsx')
json_file_path = os.path.join('src', 'data', 'sheet.json')
media_dir = os.path.join('public', 'media')

# Read the Excel file
df = pd.read_excel(file_path)

# Convert the Timestamp objects to strings
df['Timestamp'] = df['Timestamp'].astype(str)

# Function to extract image name from Google Drive link and ensure a proper filename
def extract_image_name(full_name, url):
    match = re.search(r'open\?id=([a-zA-Z0-9_-]+)', url)
    if match:
        first_name, last_name = full_name.split()[:2]
        return f"{first_name.lower()}_{last_name.lower()}.jpg"  # Ensure all saved images use .jpg
    return "default.jpg"

# Map the columns to the new format
formatted_data = []
for _, row in df.iterrows():
    full_name = row["What is your full name (Ex. John Doe)?"]
    image_url = row["Please upload an image of yourself formatted as firstname_lastname.jpg"]
    image_name = extract_image_name(full_name, image_url)

    formatted_data.append({
        "Name": full_name,
        "Role": "Exec" if row["Which of the following best describes your highest ranking role in Embedded Systems at Purdue?"] == "Officer" else row["Which of the following best describes your highest ranking role in Embedded Systems at Purdue?"],
        "DisplayCategory": row["If you are a member of exec, what is your role? If you are a Project Manager or Active Member, what project are you working on?"],
        "Image": image_name,
        "MajorYear": row["What is your major and graduation year (ex. Computer Engineering 2025)?"].replace("Computer Engineering", "CompE").replace("Electrical Engineering", "EE"),
        "LinkedIn": row["Please link your LinkedIn account"]
    })

# Save the formatted data as a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(formatted_data, json_file, indent=2)

print(f"Conversion complete: {file_path} to {json_file_path}")

# Function to check if the file matches the pattern firstname_lastname.jpg or .jpeg
def is_valid_image(filename):
    return re.match(r'^[a-z]+_[a-z]+\.(jpg|jpeg)$', filename, re.IGNORECASE)

# Function to rename files to match the pattern firstname_lastname.jpg (handling .jpeg)
def rename_image(filename):
    match = re.match(r'([a-z]+)[-_ ]([a-z]+)[-_ ]?.*\.(jpg|jpeg)$', filename, re.IGNORECASE)
    if match:
        new_name = f"{match.group(1).lower()}_{match.group(2).lower()}.jpg"  # Convert all to .jpg
        return new_name
    return None

# List all files in the media directory
for filename in os.listdir(media_dir):
    file_path = os.path.join(media_dir, filename)
    if not is_valid_image(filename):
        new_name = rename_image(filename)
        if new_name:
            new_file_path = os.path.join(media_dir, new_name)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} to {new_name}")

print("Cleanup and renaming complete.")
