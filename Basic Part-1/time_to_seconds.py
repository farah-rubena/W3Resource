'''62. Write a Python program to convert all units of time into seconds.
'''

def time_to_seconds(day, hour, mins, secs):

    day_to_sec = day * 3600 * 24
    hour_to_sec = hour * 3600
    min_to_sec = mins * 60
    sec = secs

    return day_to_sec + hour_to_sec + min_to_sec + sec

day = int(input("Enter the number of days : ")) 
hour = int(input("Enter the number of hours : ")) 
mins = int(input("Enter the number of minutes : "))
secs = int(input("Enter the seconds : "))
res = time_to_seconds(day, hour, mins, secs)
print(res)


