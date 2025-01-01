# Leap year checker

year=int(input("enter your present years: "))
if year%400==0:
    print("its leap year")
elif year%4==0 :
    if year%100!=0:
        print("it is leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year ")

# 
# sir method
year=2024
if year % 400 == 0 or ( year % 4 == 0 and year %100 !=0):
    print("leap year")
else :
    print("not a leap year")    

 