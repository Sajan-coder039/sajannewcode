# multiplication Table
number=int(input("enter the number to print table : "))

for i in range(1,11):
    if i==5:
        continue
    print(number , 'x' , i , '=' , i*number)