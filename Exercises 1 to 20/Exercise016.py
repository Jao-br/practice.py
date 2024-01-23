#Create a program that reads any Real number from the keyboard and displays its entire portion on the screen.

from math import trunc

number = float(input("Insert a number: "))
print(f"The whole part os {number} is {trunc(number)}")








# print(f"The whole part of {number} is {int(number)}")