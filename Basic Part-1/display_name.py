'''37. Write a Python program that displays your name, age, and address on three different lines.
'''

def display_details(name, age, address):

    return f"{name}\n{age}\n{address}"

name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
res = display_details(name, age, address)
print(res)