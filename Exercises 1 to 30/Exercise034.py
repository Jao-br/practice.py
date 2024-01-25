# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input("Input salary: "))

if salary > 1250.00:
    print(f"The previous salary was R${salary:.2f}\n - With a 10% raise the new compensation is R${salary * 1.10:.2f}")
else:
    print(f"he previous salary was R${salary:.2f}\n - With a 15% raise the new compensation is R${salary * 1.15:.2f}")