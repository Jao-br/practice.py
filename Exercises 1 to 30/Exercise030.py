# Create a program that reads an integer and displays on the screen whether it is ODD or EVEN.

number =  int(input("Input a number: "))

if number % 2 == 0:
    print(f"The number {number} is EVEN")
else:
    print(f"The number {number} is ODD")