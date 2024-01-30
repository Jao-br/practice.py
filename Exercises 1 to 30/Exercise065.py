# Create a program that reads several integers from the keyboard. At the end of the execution, show the average of all values ​​and which were the highest and lowest values ​​read. The program must ask the user whether or not he wants to continue typing values.
num = 0
numlist = []
numcount = 0

print("-" * 20)
print("MAX, MIN & AVARAGE CALCULATOR:")
print("To finalize the inputs and perform te claculations, input -1")

while num != -1:
    num = int(input("Input an Integer number: "))
    numlist.append(num)
    numcount += 1

print(f"You typed a total of {numcount} numbers.\nThe largest one being {max(numlist)} and the smallest {min(numlist)}.\nFurthermore, the avarage of the numbers you typed is {(sum(numlist)/numcount)}")