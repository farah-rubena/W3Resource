'''31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
It uses the Euclidean algorithm to repeatedly divide a by b and update the values of a and b until b becomes 0. 
'''

def compute_gcd(a,b):

    while b !=0 :
        a,b = b, a%b
    return a

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
res = compute_gcd(a,b)
print(res)   