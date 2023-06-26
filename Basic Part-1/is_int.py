'''36. Write a Python program to add two objects if both objects are integers.'''

def add_ints(a,b):

    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        return "Input must be Integers!!"
    
res = add_ints(10,5)
print(res)