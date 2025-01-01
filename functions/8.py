def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(power="thor like power",name="sajan sah")    
print_kwargs(name="sajan sah")   
print_kwargs(power="thor like power",name="sajan sah",enemy="hercules")   
