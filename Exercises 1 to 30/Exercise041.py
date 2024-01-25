#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

age = int(input("Input idade: "))

if age <= 9:
    print(f"Sua idede é de {age} anos, sua categoria é MIRIM")

if age <= 14:
    print(f"Sua idede é de {age} anos, sua categoria é INFANTIL")
    
if age <= 19:
    print(f"Sua idede é de {age} anos, sua categoria é JUNIOR")

if age <= 25:
    print(f"Sua idede é de {age} anos, sua categoria é SENIOR")
    
