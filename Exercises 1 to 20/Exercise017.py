# Write a program that reads the length of the opposite and adjacent sides of a right-angled triangle and calculates the length of the hypotenuse.
from math import hypot

opositeSide = float(input("Insert the trinagle´s oposite side lenght: "))
adjacentSide = float(input("Insert the trinagle´s adjacent side lenght: "))
hypotenuse = (opositeSide ** 2 + adjacentSide ** 2) ** 1/2

print(f"The lenght of the hypotenuse is {hypotenuse:.2f}")







# print(f"The lenght of the hypotenuse is {hypot(opositeSide, adjacentSide)}")
