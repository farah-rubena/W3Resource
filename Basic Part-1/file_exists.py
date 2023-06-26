'''41. Write a Python program to check whether a file exists.
The difference with previous example is that, os.path.exists() checks for the existence of file or directory, 
where as os.path.isfile() is used to check for the existence of file only.

'''

import os.path
def fileexists():

    return os.path.isfile('display_name.py')

res = fileexists()
if res:
    print("File Exists")
else:
    print("File does not exist")



