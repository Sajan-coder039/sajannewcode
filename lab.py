student={
    "id":8117913,
    "name":"sajan",
    "age":18,
    "address":'balkumari',
    "campus":"pulchowk campus",
    "grade": "bachelor",
    "faculty": "BEL",
    "books": {"physics": "2081-8-15","basic": "2081-9-18","python":"labriry read only area"

    }
}

# print(student)

student["contact"]="9814871880"


for z in student.keys():
    
    if z=="books":
        print(z,":")
        for i,j in student[z].items():
            print(f"    {i}= {j}") 
    else:
        print(f"{z}= {student[z]}")

def f(x)->None:
    print(x**2+3*x+7)

print(i)
print(j)
# f(3)









