# Write a program that reads the width and height of a wall in meters, 
# calculates its area and the amount of paint needed to paint it, 
# knowing that each liter of paint paints an area of 2 square meters.


print("-------------------------------- Paint Calculator -------------------------------- \nEnter the dimensions of your wall to see how much paint you'll need for your project.")

height = float(input(" - Insert the height of the wall you wish to paint in meters: "))
width = float(input(" - Insert the width of the wall you wish to paint, in meters"))
area = height*width
paint = area/2

print(f"You will need {paint} liters to pait your {height}m x {width}m, {area}m2 wall")
