# Develop a program that asks the distance of a trip in km. Calculate the price of the ticket, charging R$0.50 per km for trips of up to 200 km and R$0.45 for longer trips.

distance = int(input("Input the distance in KM: "))
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45