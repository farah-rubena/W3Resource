'''19. Write a Python program to get a newly-generated string from a given string where "Is" 
has been added to the front. Return the string unchanged if the given string already begins with "Is".
'''

def addis(str):

    if str[:2].lower() == "is":
        return str
    else:
        return "is" + str

str = input("Enter the string: ")
res = addis(str)
print(res)

