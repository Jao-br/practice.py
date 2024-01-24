# Write a program that reads the speed of a car. If he exceeds 80 km/h, show a message saying that he has been fined. The fine will cost R$7.00 for each km over the limit.

speed = int(input("Input the guaded speed: "))
fee = 0 

if speed > 80: 
    fee += (speed - 80) * 7
    print(f"Your car was {speed - 80} km/h over the speed limit. The fine is R${fee}")
else:
    print(f"Your car was not over the speed limit.")