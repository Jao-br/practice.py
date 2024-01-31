# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

weight = float(input('Input your weight in Kilos(kg): '))
height = float(input('Input your height in Meters(m): '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'Your Body Mass Index is of {bmi:.2f}, with is {(18.5 - bmi):.2f} points below the ideal Index.')
    print('> This BMI classifies as Below Ideal.')
elif bmi < 25: 
    print(f'Your Body Mass Index is of {bmi:.2f}, wich is at a normal weight.')
    print('> This BMI classifies as Ideal.')
elif bmi < 30:
    print(f'Your Body Mass Index is of {bmi:.2f}, with is {-1*(25 - bmi):.2f} points above the ideal Index.')
    print('> This BMI classifies as Overweight.')
elif bmi <= 40:
    print(f'Your Body Mass Index is of {bmi:.2f}, with it {-1*(25 - bmi):.2f} points above the ideal Index.')
    print('> This BMI classifies as Obesity.')
else:
    print(f'Your Body Mass Index is of {bmi:.2f}. with it {-1*(25 - bmi):.2f} points above the ideal Index.')
    print('> This BMI classifies Morbidity Obesity.')