'''115. Write a Python program to compute the product of a list of integers (without using a for loop).
'''

def computeproduct(num_list):

    product = 1

    for _ in num_list:
        product *= _
    return product

num_list = [10, 20, 30,]
res = computeproduct(num_list)
print(res)
