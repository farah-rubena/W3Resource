'''66. Write a Python program to calculate the body mass index.
'''

def calculatebmi(weight, height):

    return weight / (height **2)

weight = float(input("Enter weight in kgs: "))
height = float(input("Enter height in kgs: "))
res = calculatebmi(weight, height)
print(f"Your BMI is: {res:.2f}")