# A teacher wants to draw one of his 4 students to erase the board. Create a program that reads the students' names, draws lots and writes the chosen one on the screen.

from random import choice

student1 = input("Insert the first student´s name: ")
student2 = input("Insert the second student´s name: ")
student3 = input("Insert the third student´s name: ")
student4 = input("Insert the fourth student´s name: ")
students = [student1, student2, student3, student4]

print(f"The student chosen to erase the board is {choice(students)}")
