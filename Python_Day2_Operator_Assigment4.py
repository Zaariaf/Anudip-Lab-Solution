#Q4 Python program to find the area of a triangle whose sides are given

import math

a = 5
b = 6
c = 7

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"The area of the triangle is {area:.2f}")

#Ans=> The area of the triangle is 14.70