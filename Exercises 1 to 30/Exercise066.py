# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

ListNum = []

while True:
    num = int(input('Enter a number (or 999 to quit)'))
    if num == 999:
        break
    else:
        ListNum.append(num)


print(f'The total amount of numbers was {len(ListNum)} and its sum is {(sum(ListNum))}') 