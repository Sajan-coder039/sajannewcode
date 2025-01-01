pet=input("enter your pet species ")
age=int(input("enter your pet age:"))

if pet=="dog" and age<2:
    print("give puppy food")
elif pet=="cat" and age>5:
    print("give senior cat food")
else:
    print("give normal food")         