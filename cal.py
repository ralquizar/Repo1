import math

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
y = int(input('Enter value of y: '))


def add():
    x = a + b
    print(x)


def sub():
    x = y - b
    print(x)


print("Enter your choice: ")
print("a. Add")
print("b. Subtract")

choice = input("Enter choice: ")
if choice == 'a':
    add()
elif choice == 'b':
    sub()
else:
    print("Invalid choice")