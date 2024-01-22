#Create an algorithm that reads the price of a product
# and shows its new price, with a 5% discount.

price = float(input("Insert the price of the product: "))
discount = float(input("Insert the amount of discount without the %: "))
discountedprice = price - (price * discount / 100)

print(f"The original price was {price:.2f}, the new price with {discount:.2f}% discount is {discountedprice:.2f} dolars")
