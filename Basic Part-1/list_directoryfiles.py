'''49. Write a Python program to list all files in a directory.
'''

import os

def list_directory():

    directory_path = "C:\Users\Farah khan\Documents\Remote_Techie2023\W3Resource"

    files = os.listdir(directory_path)
    for file in files:
        if os.path.isfile(os.path.join(directory_path, file)):
            print(file)

print(list_directory())