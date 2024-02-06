# Create a program that has a pair completely filled with a count in words, from zero to ten. Your program should read a number from the keyboard (between 0 and 20) and display it in full.

numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")
while True:
    number = int(input("Enter a number between 0 and 10: "))
    if 0 <= number <= 10:
        break
    print("Try again. ", end="")
print(f"You entered {numbers[number]}.")
