'''34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
'''

def between1520(a,b):

    if a + b in range(15,21):
        return 20
    else:
        return a + b
    
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
res = between1520(a,b)
print(res)