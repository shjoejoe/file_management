import os
from PIL import Image

# Function to convert PNG to TIFF
def convert_png_to_tiff(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of PNG files in input folder
    png_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    # Process each PNG file
    for png_file in png_files:
        # Load PNG image
        png_path = os.path.join(input_folder, png_file)
        image = Image.open(png_path)

        # Extract file name without extension
        file_name = os.path.splitext(png_file)[0]

        # Save image as TIFF
        tiff_path = os.path.join(output_folder, f"{file_name}.tiff")
        image.save(tiff_path, format='TIFF')

        print(f"Converted {png_file} to {file_name}.tiff")

# Paths to input and output folders
input_folder = "/Users/shejoev/Documents/scan/Labels/20231006/Labels/Henrik/SegmentationClassProc_mergebark"
output_folder = "/Users/shejoev/Documents/scan/Labels/20231006/Labels/Henrik/SegmentationClassProc_mergebark1"

# Convert PNG to TIFF
convert_png_to_tiff(input_folder, output_folder)

print("coverting done!")
