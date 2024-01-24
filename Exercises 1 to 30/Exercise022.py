# Create a program that reads a person's full name and displays:
# - The name in all uppercase and lowercase letters.
# - How many letters in total (without taking into account spaces).
# - How many letters are in the first name.

name = input("Input name: ")

SpacelessName = len(name.replace(" ", ""))

NameList = name.split()

NameCount = len(NameList[1])


print(f"{name} in lowercase is {name.lower()} \n{name} in uppercase is {name.upper()}")
print (f"There are {SpacelessName} letters in {name.upper()}, and {NameCount} in {NameList[1].upper()}")


