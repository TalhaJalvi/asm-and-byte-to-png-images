# %% time

import numpy as np
import os
import codecs
import imageio
import array
from tqdm import tqdm
import time
from datetime import datetime as dt


root_path = 'E:\conversion from .asm,.byt to .png\\'

if not os.path.isdir(root_path + "image_file_asm"):
    os.mkdir(root_path + "image_file_asm")

asmfile_list = os.listdir(root_path + "asmFiles")


# Function to extract images from ASM files and save them to a specified folder (the second arg to the func)
def extract_images_from_text(arr_of_filenames, folder_to_save_generated_images):
    for file_name in tqdm(arr_of_filenames):
        print(arr_of_filenames)
        if (file_name.endswith("asm")):
            this_file = codecs.open(root_path + "asmFiles/" + file_name, 'rb')
            size_of_current_asm_file = os.path.getsize(root_path + "asmFiles/" + file_name)

        width_of_file = int(size_of_current_asm_file ** 0.5)

        remainder = size_of_current_asm_file % width_of_file

        # To create array of single bytes, passing type code 'B'
        # "B" is for unsigned characters
        array_of_image = array.array('B')

        array_of_image.fromfile(this_file, size_of_current_asm_file - remainder)

        this_file.close()

        arr_of_generated_image = np.reshape(array_of_image[:width_of_file * width_of_file],
                                            (width_of_file, width_of_file))

        arr_of_generated_image = np.uint8(arr_of_generated_image)

        imageio.imwrite(folder_to_save_generated_images + '/' + file_name.split(".")[0] + '.png',
                        arr_of_generated_image)


# Now invoke the above function

directory_to_save_generated_image = 'G:\\'

extract_images_from_text(asmfile_list, directory_to_save_generated_image)