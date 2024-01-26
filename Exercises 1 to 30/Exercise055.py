# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos=[]
for i in range(1,6):
    num = float(input("Digite um peso: "))
    pesos.append(num)

print(f"O maior peso foi {max(pesos):.2f} e o menor peso foi {min(pesos):.2f}")