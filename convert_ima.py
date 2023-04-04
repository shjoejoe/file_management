import os
import numpy as np
import tifffile as tif
from skimage import io

# Define the paths to your source and destination folders
src_folder = '/Users/shejoev/Documents/scan/CT-1/ref_stock_2023/convert_file_format/pine_1'
dest_folder = '/Users/shejoev/Documents/scan/CT-1/ref_stock_2023/convert_file_format/tiff_pine_1'


# Get a list of all files in the source folder
files = os.listdir(src_folder)


# Get a list of all files in the source folder
files = os.listdir(src_folder)


# Loop through the sorted list of files, read them as NumPy arrays, and export them as TIFF files
for f in files:
    src_path = os.path.join(src_folder, f)
    dest_path = os.path.join(dest_folder, os.path.splitext(f)[0] + '.tiff')
    
    # Read the image as a NumPy array using skimage.io.imread()
    img = io.imread(src_path, plugin='simpleitk')
    
    # Export the image as a TIFF file using skimage.io.imsave()
    io.imsave(dest_path, img)