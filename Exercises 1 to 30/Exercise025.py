# Create a program that reads a person's name and tells if they have "SILVA" in their name.

name = input("Input a name: ")

if "silva" in name.lower():
    print(f"{name.upper()}contains silva")
else:
    print(f"{name.upper()}does NOT contais silva")