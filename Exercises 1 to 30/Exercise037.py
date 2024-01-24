# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input("Input a number: "))

print("Choose one of the options below to convert the number you typed in:")
print("[1] - Convert to binary")
print("[2] - Convert to octal")
print("[3] - Convert to hexadecimal")

option = int(input("Option: "))

if option == 1:
    print(f"{number} converted to binary is {bin(number)}")
elif option == 2:
    print(f"{number} converted to octal is {oct(number)}")
elif option == 3:
    print(f"{number} converted to hexadecimal is {hex(number)}")
else:
    print("Invalid option!")