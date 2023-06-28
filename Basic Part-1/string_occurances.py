'''84. Write a Python program to count the number of occurrences of a specific character in a string.
'''

def stringoccurances(text, letter):

    count = 0

    for _ in text:
        if _ == letter:
            count += 1

    return count

text = input("Enter the string: ")
letter = input("Enter the alphabet to be checked: ")
res = stringoccurances(text, letter)
print(res)
