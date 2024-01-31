# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Insira um número para calcular sua tabuada: "))
value = 0

for i in range(0, 11):
    print(f"{num} X {value} = {num * value}")
    value += 1

