# factorial of the Number for loop method:
fact=1
num=int(input("enter the number:"))

# for i in range(1,num+1):
#     fact=fact*i
    
# print(fact)

# while loop method
while num>0:
    fact=fact*num#fact*=num
    num=num-1#num-=1

print(fact)
