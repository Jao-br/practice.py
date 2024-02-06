# Create a program that simulates the operation of an ATM. At the beginning, ask the user what amount will be withdrawn (whole number) and the program will inform how many bills of each amount will be delivered.
# NOTE: consider that the cashier has banknotes worth R$50, R$20, R$10 and R$1.


print("="*30)
print(f"{'CASHIER':^30}")
print("="*30)
valor = int(input('Enter a value to pay: R$'))
cédula = 50
total = valor
cedulas = 0
while True:
    if total >= cédula:
        total -= cédula
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Total of {cedulas} R${cédula} notes')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        cedulas = 0
        if total == 0:
            break
print("="*30)