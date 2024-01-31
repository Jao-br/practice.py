# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

price = float(input('Input produt price: R$'))

print(f'Digite o número da opção de pagamento desejada:\n [1] À vista dinheiro/cheque:  10% Off.\n [2] À vista no cartão:  5% Off.\n [3] Em até 2x no cartão:  Preço Formal\n [4] 3x ou mais no cartão:  20% de Juros sob o Montante Total')
pay_method = int(input('Opção: '))

if pay_method == 1:
    price = price * 0.9
elif pay_method == 2:
    price = price * 0.95
elif pay_method == 3:
    price = price 
elif pay_method == 4:
   price = price * 1.2
else: 
    print("Invalid payment method")

print(f'The Fina Price is: R${price}')

