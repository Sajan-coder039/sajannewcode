# sum of Even numbers
even_number=int(input("enter n:"))
sum=0
for num in range(0,even_number+1):
    if num%2==0:
        sum=sum+num
print(sum)        