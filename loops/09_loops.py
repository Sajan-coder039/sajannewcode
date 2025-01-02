items=["apple","banana","orange","apple","mango","apple","apple","apple"]


unique_item=set()
dupli_no=0
for item in items:
    if item in unique_item:
        print("duplicate: ",item)
        
        break
    unique_item.add(item)

dupli_no+=1
print(dupli_no)
# for string1 in items:
#     if items.count(string1)==2:
#         print(string1)
#         break