# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input("Input house value: "))
salary = float(input("Input Salary: "))
years = int(input("Input how many years you will take to pay the house: "))

if (house_value / (years * 12) > (salary * 0.30)):
    print("The loan was denied!")
else:
    print(f"Your ${house_value:.2f} in {years} years loan was aproved!")