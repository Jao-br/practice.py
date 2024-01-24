# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Input the first side of the triangle: "))
b = float(input("Input the second side of the triangle: "))
c = float(input("Input the third side of the triangle: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("The values you typed in CAN form a triangle!")
else:
    print("The values you typed in CAN´T form a triangle")