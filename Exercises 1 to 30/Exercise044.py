# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

price = float(input('INSIRA O VALOR DO PRODUTO: R$'))

print('-' * 60)
print(f'> Tabela de Descontos/Acréscimos:\n - À vista dinheiro ou cheque:  10% Off.\n - À vista no cartão:  5% Off.\n - Em até 2x no cartão:  Preço Formal\n - 3x ou mais no cartão:  20% de Juros sob o Montante Total')
print('-' * 60)
print('> Escolha a Forma de Pagamento desejada:\n [1] para Dinheiro à vista.\n [2] para Cheque à vista.\n [3] para Cartão.')
pay_method = int(input('Opção: '))

if pay_method in (1,2):
    price = price * 0.9
elif pay_method == 3:
    parcelas = int(input(f'Insira o número de parcelas: '))
    if parcelas == 1:
        price = price * 0.95
    elif parcelas == 2:
        price = price
    elif parcelas > 2: 
        price = price * 1.20 
else: 
    print("OPÇÃO INVÁLIDA!")

print('-' * 60)
print(f'PREÇO FINAL: R${price}')