#Write a program that converts a temperature you type into degrees Celsius and converts it to degrees Fahrenheit.

print("-------------------------------- Temperature Converter -------------------------------- \nInsert a temperature in Celsius to convert it to Fahrenheit.")

celsius = float(input(" - Insert the temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}ºC is equivalent to {fahrenheit}ºF")