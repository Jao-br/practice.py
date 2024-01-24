#Create an algorithm that reads an employee's salary and shows his new salary, with a 15% increase.

salary = float(input("Insert the current salary: $"))
salaryRaise = float(input("Insert the deisered raise: "))
newSalary = salary + (salary * salaryRaise / 100)

print(f"The original salary was ${salary:.2f}.\n The new salary with {salaryRaise:.2f}% raise is ${newSalary:.2f} dollars")