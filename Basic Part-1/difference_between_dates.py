'''14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import date

def diff_dates():

    f_date = date(2014, 7, 2)
    s_date = date(2014, 7, 11)
    return s_date - f_date

res = diff_dates()
print(res)

