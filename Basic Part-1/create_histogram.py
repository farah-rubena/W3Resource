'''26. Write a Python program to create a histogram from a given list of integers.
'''

def histogram(char, numlist):

    histogram = ""
    for _ in numlist:
        histogram += char * _ + "\n" 
    return histogram

char = input("Enter a character: ")
numlist = [2,3,6,5]
res = histogram(char,numlist)
print(res)

