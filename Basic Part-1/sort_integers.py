'''69. Write a Python program to sort three integers without using conditional statements and loops.
'''

def sortint(n1, n2, n3):

    lowest = min(n1, n2, n3)
    highest = max(n1, n2, n3)
    middle = (n1 + n2 + n3) - lowest - highest 
    return lowest, middle, highest 

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
res = sortint(n1, n2, n3)
print(res)