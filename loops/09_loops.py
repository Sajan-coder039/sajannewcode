items=["apple","banana","orange","apple","mango"]

# for string1 in items:
#     if items.count(string1)==2:
#         print(string1)
#         break



unique_item=set()

for item in items:
    if item in unique_item:
        print("duplicate: ",item)
        break
    unique_item.add(item)


