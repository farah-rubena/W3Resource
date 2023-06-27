'''50. Write a Python program to print without a newline or space.
'''

def print_withoutspace(num):

    for _ in range(num):
        print(_, end="")
    
num = int(input("Enter a number: "))
print_withoutspace(num)