'''114. Write a Python program to filter positive numbers from a list.
'''


def find_positive(num_list):

    positive = []
    for _ in num_list:
        if _ > 0:
            positive.append(_)
    return positive

num_list = [34, 1, 0, -23, 12, -88]
res = find_positive(num_list)
print(res)