username="chaiaurcode"

def func():
    username="chai"
    print(username)

print(username)  
func()  
# sdfghjkl;sdfghjkldfghjkl
x=99

def func2(y):
    z=x+y
    return z

result=func2(1)
print(result)

def func3():
    global x #global new keyword♥☻
    x=123

func3()
print(x)    

def f1():
    # x=9
    def f2():
        print(x)
    f2()
f1()        

def chai(num):
    def coder(x):
        return x**num
    return coder

