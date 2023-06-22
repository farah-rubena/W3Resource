'''8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''

def first_last():
    
    color_list = ["Red","Green","White" ,"Black"]

    return color_list[0], color_list[-1]

res = first_last()
print(res)  