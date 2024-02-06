# Create a program that reads the name and price of several products. The program should ask whether the user will continue or not. At the end, show:
# A) what is the total spent on the purchase.
# B) how many products cost more than R$1000.
# C) what is the name of the cheapest product.

total = expensive = cheaper = 0
cheapest_product = ""
while True:
    product = str(input("Product: "))
    price = float(input("Price: R$"))
    total += price
    if price > 1000:
        expensive += 1
    if cheaper == 0 or price < cheaper:
        cheaper = price
        cheapest_product = product
    cont = " "
    while cont not in "YN":
        cont = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
    if cont == "N":
        break
print("\nTotal spent: R${:.2f}".format(total))
print("Products that cost more than R$1000: {}".format(expensive))
print("Cheapest product: {} - R${:.2f}".format(cheapest_product, cheaper))
print("\nEnd of the program")