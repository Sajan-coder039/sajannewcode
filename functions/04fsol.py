def thaepi (radius):
    area=3.14*(radius**2)
    circum=3.14*2*radius
    return area,circum

area,perimeter =thaepi(7)

print("area: ",area ,"circumference: ",perimeter)

# we can use module 
# import math
# math.pi