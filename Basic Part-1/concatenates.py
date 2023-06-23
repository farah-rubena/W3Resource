'''27. Write a Python program that concatenates all elements in a list into a string and returns it.
'''

def concatenate_all(lst):

    for _ in lst:
        num_as_string = [str(_) for _ in lst]
        result = "".join(num_as_string)
    return result

lst = [1,5,12,2]
res = concatenate_all(lst)
print(res)
