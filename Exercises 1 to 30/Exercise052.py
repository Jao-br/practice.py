# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            Jorge = True
        else:
            Jorge = False   
elif num == 0:
    print(f"{num} é zero")
elif num == 1:
    print(f"{num} é um")
else:
    print(f"{num} é negativo")
    
    
if Jorge == True:
    print("O numero não é primo")
else:
    print("O numero é primo")