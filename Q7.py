import math
r = int(input("Enter your radius of Sphere : "))
AreaS = 4*math.pi*(r*r)


r = int(input("Enter your radius of Cylinder : "))
h = int(input("Enter your height of Cylinder : "))
AreaH = 2*math.pi*(r*r) + 2*math.pi*r*h

l = int(input("Enter your length of Cuboid: "))
b = int(input("Enter your breadth of Cuboid: "))
h = int(input("Enter your height of Cuboid: "))
AreaC = 2*(l*b + b*h + h*l)


print("Sphere Area : ",AreaS)
print("Cylinder Area : ",AreaH)
print("Cuboid Area : ",AreaC)