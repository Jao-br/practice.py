#  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

letra = str(input("Insira valores F ou M: ")).upper()

while letra not in "FM":
    print("Valor incorreto, Digite novamente!")
    break
    
print("valor correto!, obrigado.")