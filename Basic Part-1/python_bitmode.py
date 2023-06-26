'''42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
'''
#('64bit', 'WindowsPE')

import platform

def check_pythonbitmode():
    
    if platform.architecture()[0] == "32bit":
        return "32 Bit"
    elif platform.architecture()[0] == "64bit":
        return "64 Bit"
    else:
        return "Unknown"

res = check_pythonbitmode()
print(res)

        
