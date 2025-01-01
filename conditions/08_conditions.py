# Password strength checker 
password=input("enter your password (only alphabets now) :")

if len(password)<6:
    print("weak ")
elif len(password)<10:
    print("medium")
else:
    print("strong")