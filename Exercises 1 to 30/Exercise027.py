# Write a program that reads a person's full name, then shows the first and last names separately.

name = input("Input full name: ").upper()
nameList = name.split()

print(f"Your fisrt name is {nameList[0]} and your last is {nameList[-1]}")