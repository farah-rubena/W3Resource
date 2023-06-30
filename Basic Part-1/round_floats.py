'''119. Write a Python program to round a floating-point number to a specified number of decimal places.
'''

def roundfloats(num, decimalplace):

    return f"{num:.{decimalplace}f}"


num = float(input("Enter a number: "))
decimalplace = int(input("Enter the decimal places: "))
res = roundfloats(num, decimalplace)
print(res)  