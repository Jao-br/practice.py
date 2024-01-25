# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sex = str(input("Digite [M] para Masculino\nDigite [F] para Feminino\n Input sexo: ")).upper()

if sex == "F":
    print("Você não precisa se alistar, Mocinha!")

else:
    dayOfBirth = int(input("Digite o seu  nascimento: "))
    PresentYear = date.today().year
    age = PresentYear - dayOfBirth 

    if age > 18:
        print(f"Ainda faltam {age - 18} anos para o seu alistamento.")

    elif age == 18: 
        print(f"Você tem exatos {age} anos, Soldado! Chegou a hora do seu Alistamento")

    elif age < 18: 
        print(f"Seu alistamento está {age - 18} anos atrasado soldado! Procure a juta militar mais proxima a sua casa para realizar seu alistamento.")

    elif age < 45:
        print()