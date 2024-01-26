# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import choice

num = [1,2,3,4,5,6,7,8,9,10]
contador = 1
fim = 1000

for i in range(0,fim):
    computador = choice(num)
    jogador = int(input("Escolha um número de 1 a 10: "))
    if jogador == computador:
        print(f"Você adivinhou o número com {contador} tentativas")
        contador += 1
        break
    elif jogador > 10:
        print("O número deverá estar entre 1 a 10!!")
    else:
        print("Você errou o número")
        contador += 1