# Write a program that reads any angle and displays the sine, cosine and tangents of that angle on the screen.

from math import sin, cos, tan, radians

angle = float(input("Insert the angle: "))
radians = radians(angle)
sine_value = sin(radians)
cosine_value = cos(radians)
tangent_value = tan(radians)

print(f"The sine of {angle}º is {sine_value:.2f}")
print(f"The cosine of {angle}º is {cosine_value:.2f}")
print(f"The tangent of {angle}º is {tangent_value:.2f}")
