# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = float(input("Input the first side of the triangle: "))
b = float(input("Input the second side of the triangle: "))
c = float(input("Input the third side of the triangle: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("The values you typed in CAN form a triangle!")
elif a == b == c:
    print("O triangulo formado é Equilatero")
elif (a == b != c) or (a == c != b) or (b == c != a):
    print("O triangulo formado é Isóceles")
elif a != b !=c: 
    print("O triangulo formado é ESCALENO")
