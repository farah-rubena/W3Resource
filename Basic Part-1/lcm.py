'''Find the greatest common divisor (GCD) of the numbers.
Divide the product of the numbers by their GCD.
The result will be the LCM of the numbers.

'''

def find_gcd(a,b):

    while b !=0 :
        a,b = b, a%b
    return a

def find_lcm(a,b):
    return (a*b)//find_gcd(a,b)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
res = find_lcm(a,b)
print(res)

