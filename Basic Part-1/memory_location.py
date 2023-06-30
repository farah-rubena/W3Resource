'''117. Write a Python program to prove that two string variables of the same value point to the same memory location.
could also use hex(id(str1)) to find the hexadecimal id
'''

def location(str1, str2):

    if str1 is str2:
        return "Point to the same Memory Location"
    else:
        return "Do not point to the same Memory Location"

str1 = input("Eneter value : ")
str2 = input("Eneter value : ")
res = location(str1, str2)
print(res)