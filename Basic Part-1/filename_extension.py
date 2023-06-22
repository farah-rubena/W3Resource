'''7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

def filenameextension(name):

    extension = name.split(".")
    return extension[-1]

res = filenameextension("abc.java")
print(res)