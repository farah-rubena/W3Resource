'''30. Write a Python program that will accept the base and height of a triangle and compute its area.
'''


def area(base, height):

    return base * height / 2

base = float(input("Enter the base of the tiangle : "))
height = float(input("Enter the height of the tiangle : "))
res = area(base, height)
print(res)
