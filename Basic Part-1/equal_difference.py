'''35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
'''
def equal_diff(a,b):

    if a == b or a + b == 5 or abs(a-b) == 5:
        return True
    else:
        return False

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))    
res = equal_diff(a,b)
print(res)