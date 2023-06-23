'''29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''

def uniquecolors(color_list1, color_list2):

    return color_list1 - color_list2

color_list1 = set(["White", "Black", "Red"])
color_list2 = set(["Red", "Green"])
res = uniquecolors(color_list1, color_list2)
print(res)