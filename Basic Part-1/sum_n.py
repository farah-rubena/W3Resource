'''58. Write a Python program to sum the first n positive integers.
'''

def sum_of_n(num):
    sum = 0
    for _ in range(num+1):
        sum += _
    return sum

num = int(input("Enter a number: "))
res = sum_of_n(num)
print(res)