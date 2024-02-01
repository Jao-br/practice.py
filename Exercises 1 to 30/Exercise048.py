# Faça um programa que calcule a soma entre todos ímpares os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

ListNum = []
for i in range(0,500):
    if i % 2 != 0:
        if ( i% 3 ==0 ):
            ListNum.append(i)

print(ListNum)
print(sum(ListNum))