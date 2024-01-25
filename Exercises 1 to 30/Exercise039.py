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
        print("Jã passou da hora de você se alistar SOLDADO !")

        tempo_passou =  age - 18
        print("Você deveria ter se alistado a {} anos, vá ao posto de alistamento mais proximo !".format(tempo_passou))