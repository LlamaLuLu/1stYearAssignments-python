# Takes lengths of sides of triangle & calculates its area
# Lulama Lingela
# 24 February 2023

import math

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
    print("Error: The input does not describe a triangle.")
else:
    heron_s = (side1 + side2 + side3) / 2
    area = math.sqrt(heron_s * (heron_s - side1) * (heron_s - side2)  * (heron_s - side3))    
    print(f"The area of the triangle with sides of length {side1} and {side2} and {side3} is {round(area, 2)}.")