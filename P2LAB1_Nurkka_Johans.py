# Johans Nurkka
# February 16, 2026
# P2LAB1
# Program that calculates a circle's diameter, circumference, area,
# and the volume of a sphere given a user-provided radius

import math

# Get a radius from user as a float

radius = float(input("Enter the radius of the circle: "))
print()


# Calculate diamteter

diameter = 2 * radius

# Calculate circumference

circumference = 2 * radius * math.pi

# Calculate area

area = math.pi * radius ** 2

#Claculate volume of sphere

sphere = 4/3 * math.pi * radius ** 3

# Display results for diameter circumference and area

print(f"The diameter of the circle is: {diameter: .1f}")
print()
print(f"The circumference of the circle is: {circumference: .2f}")
print()
print(f"The area of the circle is: {area: .3f}")
print()
print(f"The volume of the sphere is: {sphere: .4f}")
print()