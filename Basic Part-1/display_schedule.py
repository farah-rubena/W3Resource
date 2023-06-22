'''9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

def displayschedule(date, month, year):

    return f"{date}/{month}/{year}"

res = displayschedule(11,12,2014)
print(res)