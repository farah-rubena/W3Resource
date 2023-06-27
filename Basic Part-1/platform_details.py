'''43. Write a Python program to get OS name, platform and release information.
'''

import platform

def get_platform_details():

    # get OS details
    os_name = platform.system()

    # get platform details
    platform_name = platform.platform()

    #get release information
    release_info = platform.release()

    return os_name, platform_name, release_info

res = get_platform_details()
print(res)