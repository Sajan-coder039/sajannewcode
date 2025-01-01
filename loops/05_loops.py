# Given a string , find the non-repeated character
string="teetertenks"

for char in string:
    if string.count(char)==1:
        print("non repeated character is ",char)
       


