radius = float(input("Enter the radius of the circle: "))

area = 3.14*radius**2
circumference = 2*3.14*radius
area_of_smallest_square_covers = (2*radius)**2
area_of_largest_square_fits = (2**1/2*radius)**2

print("Area of the circle:", area)
print("Cİrcumference of the circle:", circumference)
print("Area of the smallest square that covers this circle:",area_of_smallest_square_covers)
print("Area of the largest square that fits in this circle:",area_of_largest_square_fits)