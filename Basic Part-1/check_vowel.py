'''24. Write a Python program to test whether a passed letter is a vowel or not.'''

def checkvowel(letter):

    if letter in ['a','e','i','o','u']:
        return "vowel"
    else:
        return "not vowel"

l = input("Enter the letter to be checked: ").lower()
res = checkvowel(letter=l)
print(res)