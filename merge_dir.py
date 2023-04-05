import imageio
import os
from PIL import Image
from resizeimage import resizeimage
import numpy as np 

path = "/Users/shejoev/Documents/scan/CT-1/log_1-1/Denoised" # change this to your folder path
image_path_list = os.listdir(path) # get a list of all files in the folder
image_path_list.sort()
print(image_path_list)
with imageio.get_writer("new_image.tiff") as new_image: # create a new .tiff image

    for image_path in image_path_list: # loop through each file
        if image_path.endswith(".tiff") or image_path.endswith(".tif"): # check if it is a .tiff file
            with open(path + "/" + image_path, "r+b") as f: # open the file as binary mode
                with Image.open(f) as image: # read the file as an image using PIL
                    resized_image = resizeimage.resize_cover(image, [200, 200]) # resize the image to 200x200 pixels other values are applicable
                    resized_array = np.asarray(resized_image) # convert the resized image to a numpy array using numpy.asarray()
                    new_image.append_data(resized_array) # append the resized array data to the new image inside the with block




