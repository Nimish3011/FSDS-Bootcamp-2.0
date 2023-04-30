"""
4. Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504

"""

from math import pi
f = float(input("Enter the radius of the circle : "))
print("The area of the circle with radius " + str(f) + " is : " + str(pi * f**2)) 