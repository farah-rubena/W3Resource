'''3. Write a Python program to display the current date and time.
'''
#datetime module is a part of Python's Standard Library


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
