# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

evenNumList = []
oddNumList = []

for i in range(0,6):
    num = int(input('Type an even number (Odd numbers will be disconsidered): '))
    if num % 2 == 0:
        evenNumList.append(num)
    else:
        oddNumList.append(num)

print(f'The sum of the even numbers {sum(evenNumList)}')
print(f'The Odd numbers you mistakenly typed are {oddNumList}')
