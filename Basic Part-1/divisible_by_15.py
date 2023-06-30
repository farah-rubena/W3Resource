'''110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
x%15==0 is the expression
returns x
'''

num_list = [45, 55, 60, 37, 100, 105, 220]

result = list(filter(lambda x: x%15 == 0, num_list))

print(result)