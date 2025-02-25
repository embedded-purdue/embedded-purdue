import os
from pillow_heif import open_heif
from PIL import Image

# Define the input and output paths
input_folder = "src/media/input"
output_folder = "src/media/upload"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        input_path = os.path.join(input_folder, filename)
        
        # Open the HEIC file
        heif_file = open_heif(input_path)
        
        image = heif_file.to_pillow()
        
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_filename)
        image.save(output_path, "JPEG")
        
        print(f"Conversion complete: {input_path} to {output_path}")