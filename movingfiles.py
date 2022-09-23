import os
# importing shutil module
import shutil

#separating byte files and asm files
source = 'image_file_bytes'

destination_1 = 'Ramnit'
destination_2 = 'Lollipop'
destination_3 = 'Kelihos_ver3'
destination_4 = 'Vundo'
destination_5 = 'Simda'
destination_6 = 'Tracur'
destination_7 = 'Kelihos_ver1'
destination_8 = 'Obfuscator.ACY'
destination_9 = 'Gatak'


# we will check if the folders exists if it not there we will create a folder with the same name
if not os.path.isdir(destination_1):
    os.makedirs(destination_1)
if not os.path.isdir(destination_2):
    os.makedirs(destination_2)
if not os.path.isdir(destination_3):
    os.makedirs(destination_3)
if not os.path.isdir(destination_4):
    os.makedirs(destination_4)
if not os.path.isdir(destination_5):
    os.makedirs(destination_5)
if not os.path.isdir(destination_6):
    os.makedirs(destination_6)
if not os.path.isdir(destination_7):
    os.makedirs(destination_7)
if not os.path.isdir(destination_8):
    os.makedirs(destination_8)
if not os.path.isdir(destination_9):
    os.makedirs(destination_9)

# Reading excel file for labels and file names,  moving them in corresponding label folders
import pandas as pd

col_list = ["Id", "Class"]
df = pd.read_csv('trainLabels.csv', usecols=col_list)
i = 0
if os.path.isdir(source):
    datafiles = os.listdir(source)
    for files in datafiles:
        for i in range(len(df["Id"])):
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 1)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_1)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 2)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_2)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 3)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_3)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 4)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_4)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 5)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_5)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 6)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_6)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 7)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_7)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 8)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_8)
            if ((files.split(".")[0]==df["Id"][i]) & (df["Class"][i] == 9)):
                print(files.split(".")[0])
                shutil.move(source + '\\' + files, destination_9)




