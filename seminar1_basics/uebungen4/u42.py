import math

print("Übung 4.2")

radius = float(input("enter radius (end <= 0) > "))

while radius > 0:
    perimeter = 2 * radius * math.pi
    area = radius * radius * math.pi
    print("Radius:", radius, "Area:", area, "Perimeter:", perimeter)
    radius = float(input("enter radius (end <= 0) > "))
