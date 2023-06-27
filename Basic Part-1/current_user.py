'''54. Write a Python program to get the current username.
'''

import getpass

def currentuser():

    return getpass.getuser()

res = currentuser()
print(res)
