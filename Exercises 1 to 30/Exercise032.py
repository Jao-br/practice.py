# Make a program that reads any year and shows whether it is a leap year.

year = int(input("Input Year: "))
if year % 4 == 0:
    print(f"The year {year} is Leap Year")
    
else:
    print(f"{year} Is NOT a leap Year")