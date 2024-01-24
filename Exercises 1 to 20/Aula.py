# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente, 
# de um triângulo retângulo, e calcule o comprimento da hipotenusa. 

from math import hypot 
catetoOposto = int (input ("Digite o cateto Oposto? "))
catetoAdjacente= int ((input ("Digite o cateto Adjacente? ")))
hipotenusa= hypot (catetoOposto, catetoAdjacente)

print(f"A hip desse triângulo será {hipotenusa:.4f}")
