# 64) Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = qtd = 0
while True:
    numeros = int(input("insira o número >> "))
    if (numeros != 999):
        soma += numeros
        qtd += 1
        print('Você adicionou mais um numero')
    else:
        print(f"A soma de todos os números inseridos é igual: {soma}, e o total digitado foi: {qtd}")
        break
