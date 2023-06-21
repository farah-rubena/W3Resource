'''4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
'''

def circlearea(radius):

    pi = 3.14159

    return pi*(radius**2)

r = float(input("Enter the radius of the circle: "))
res = circlearea(radius=r)
print(res)