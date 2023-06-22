'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

def builtin_description(func):
    
    return help(func)

func = input("Enter the in-built function: ")
res = builtin_description(func)
print(res)