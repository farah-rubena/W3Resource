'''38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''


def solve_equation(x,y):

    return (x + y) ** 2

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
res = solve_equation(x,y)
print(res)