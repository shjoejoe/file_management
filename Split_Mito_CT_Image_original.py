# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:46:25 2022
@author: Yunbo Huang
##### Split the tiff file from Microtec scanner, extract the scanning parameters, e.g., KeV,current, voxel size
"""
# %% import modules
import os
import tifffile
import numpy as np
from datetime import datetime


# %%
def Split_slices(dir_tiff, Tiff_names, boolean_expoert_3D_array):
    for name in Tiff_names:
        print("Now working with file: %s" % (name))
        before_time = datetime.now()
        case_path = dir_tiff + "\\_%s_slices" % (name[:-5])  ### Create a new folder
        if not os.path.exists(case_path):
            os.makedirs(case_path)

        #### While opened with tifffile, the file is divided into two series.
        #### f.series[0] contains the actual data, either in the form of multiple pages (slices)
        #### or one stiched page. f.series[1] contains the scanning parameters, ASCII encoded.

        with tifffile.TiffFile(dir_tiff + "\\" + name) as f:
            if len(f.pages) > 2:
                imgs = f.series[0].asarray()
                slice_num, height, width = imgs.shape
            else:
                imgs = f.pages[0].asarray()
                width = imgs.shape[1]
                height, slice_num = f.pages[0].tags["PageNumber"].value
                imgs = imgs.reshape(slice_num, height, width)
            scanning_para = f.pages[-1].asarray()[
                0
            ]  #### it is a 2D array(1,1241) array, we only need it to be 1D.
            f.close()
        imgs = imgs.astype("uint16")
        # string_scanning_para = "".join(list(chr(i) for i in scanning_para)) ### usefull only if you want to attach scanning parameter to each slice

        #### Split to  slices
        file_name_length = len(
            str(slice_num)
        )  ### just make it easier to name the slices
        for i in range(slice_num):
            tifffile.imwrite(
                case_path
                + "\\%s_%s.tiff" % (name[:-5], str(i).zfill(file_name_length)),
                np.swapaxes(imgs[i], 0, 1),
                dtype="uint16",
                photometric="minisblack",  # compression = ,\   ### set compression
                # metadata={"scanning_parameter":string_scanning_para},\ ### attach scanning parameter to each slice
                #### more possibilities here
            )
        ### Write scanning parameter to .txt,
        with open(case_path + "\\Scanning_information.txt", "w") as f:
            for i in scanning_para:
                f.write(chr(i))  ### ASCII

        #### Export as 3D array
        if boolean_expoert_3D_array:
            tifffile.imwrite(
                case_path + "\\3D_array_%s" % (name),
                np.swapaxes(imgs, 1, 2),
                dtype="uint16",
                photometric="minisblack",  # compression = ,\   ### set compression
                # metadata={"scanning_parameter":string_scanning_para},\ ### attach scanning parameter to each slice
            )
        print(
            "####### %s finished, time taken: %d s\n\n"
            % (name, (datetime.now() - before_time).total_seconds())
        )


# %% Define variables

### The folder directory
dir_tiff = r"containning folder here"
### Incase multiple tiff files are to be handled, otherwise specify name manually.
### NB: all tiff within the folder will be handled
Tiff_names = list(i for i in os.listdir(dir_tiff) if ".tiff" in i)
### Incase want to export 3D array
boolean_expoert_3D_array = True


Split_slices(dir_tiff, Tiff_names, boolean_expoert_3D_array)
