# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das seguintes mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))

if number1 > number2:
    print(f"The firts value ({number1}) is greater than the second ({number2})")
elif number2 > number1:
    print(f"The second value ({number2}) is greater than the first ({number1})")
else:
    print("There is no greater value, both are equal")