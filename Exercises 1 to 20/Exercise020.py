# The same teacher from the previous challenge wants to draw the order in which the students' work will be presented. Make a program that reads the names of the four students and displays the order drawn.

from random import shuffle

student1 = input("Insert the first student´s name: ")
student2 = input("Insert the second student´s name: ")
student3 = input("Insert the third student´s name: ")
student4 = input("Insert the fourth student´s name: ")
students = [student1, student2, student3, student4]

print(f"The order is {shuffle(students)}")
