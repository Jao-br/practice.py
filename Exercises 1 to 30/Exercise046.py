# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

print('FIREWORK COUNTDOWN:')
num = 10 
for i in range(num, -1, -1):
    sleep(1)
    print(f'{i} seconds missing')
    