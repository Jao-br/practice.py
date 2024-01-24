#Write a program that asks for the number of kilometers traveled by a rented car and the number of days for which it was rented. Calculate the price to pay, knowing that the car costs BRL 60 per day and BRL 0.15 per km.

print("-------------------------------- Car Rental Calculator -------------------------------- \nInsert the number of days and kilometers traveled to calculate the total price of your rental.")
days = int(input(" - Insert the number of days you rented the car: "))
km = float(input(" - Insert the number of kilometers traveled: "))
price = (days * 60) + (km * 0.15)

print(f"The total cost of your {days} days and {km:.2f}km rental is R${price:.2f}")