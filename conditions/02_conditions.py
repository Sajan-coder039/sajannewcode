age=int(input("enter your age:"))
day=input("enter day:")
price=0

if age>=18 :
    price=12
else :
    price= 8

if day=="wednesday":
    price=price-2           #or price-=2

print("ticket price for you $ ",price)
