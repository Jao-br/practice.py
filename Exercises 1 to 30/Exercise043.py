# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('-'*10,'BODY MASS INDEX CALCULATOR','-'*10)
print('\n-SELECT YOUR SYSTEM OF UNITS:\n  > [1] for METRIC\n  > [2] for IMPERIAL')

units = int(input('Insert the desired number: '))

if units == 1:
    weightM = float(input('Input your weight in Kilos(kg): '))
    heightM = float(input('Input your height in Meters(m): '))
    bmi = weightM / (heightM ** 2)

    if bmi < 18.5:
        print(f'Your Body Mass Index is of {bmi:.2f}, with is {(18.5 - bmi):.2f} points below the ideal Index.')
        print('> This BMI classifies as Below Ideal.')
    elif bmi < 25: 
        print(f'Your Body Mass Index is of {bmi:.2f}.')
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

elif units == 2:
    weightI = float(input('Input your weight in Pounds(lb): '))
    covertedWeigth = weightI * 0.45359237
    
    heightI = float(input('Input your height in Feet(ft): '))
    convertedHeight = heightI * 0.3048

    bmi = covertedWeigth / (convertedHeight ** 2)

    if bmi < 18.5:
        print(f'Your Body Mass Index is of {bmi:.2f}, with is {(18.5 - bmi):.2f} points below the ideal Index.')
        print('> This BMI classifies as Below Ideal.')
    elif bmi < 25: 
        print(f'Your Body Mass Index is of {bmi:.2f}.')
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

else:
    print('INVALID SYSTEM SELECTED')