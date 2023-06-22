'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''

def compute_num(a):

    a1 = f"{a}"
    a2 = f"{a}{a}"
    a3 = f"{a}{a}{a}"
    #print(type(a3))
    add = int(a1) + int(a2) + int(a3)
    return add

num = int(input("Enter a number: "))
res = compute_num(a=num)
print(res)