# Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to figure out which number the computer chose. The program should write on the screen whether the user won or lost.

from random import choice

numbers = [1,2,3,4,5]
num = int(input("Guess a number between 1 and 5: "))
randomNum = choice(numbers)
    
    
if num == randomNum:
    print("YOU WON!!")
else:
    print(f"YOU LOST, THE NUMBER WAS {randomNum} TRY AGAIN NEXT TIME")

