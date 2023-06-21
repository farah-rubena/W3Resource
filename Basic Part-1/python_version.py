'''Write a Python program to find out what version of Python you are using.'''

import platform

def pythonversion():

    version = platform.python_version()
    print(version)

pythonversion()

