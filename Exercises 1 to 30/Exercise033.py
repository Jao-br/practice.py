# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numbers = []
n = str(input("Input 3 diferent numbers separated by spaces: "))

for i in n.split():
    numbers.append(int(i))

print(f"The largest number you typed in is {max(numbers)} and the smallest is {min(numbers)}")
