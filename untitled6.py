r1 = float(input("Enter the first circle's radius: "))
r2 = float(input("Enter the second circle's radius: "))

blue_area = ((2*r1+2*r2)/2)**2*3.14-r1**2*3.14-r2**2*3.14

print("Blue area:", blue_area)