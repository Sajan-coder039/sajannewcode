#my first project

import time

wait_time=1  #(in second)
max_attemps=5
attemps=0
real_password="sajansah123"
while (attemps<max_attemps):
    password=input("enter your phone pin: ")
   
    
    if (password==real_password):
        print("your phone unlock☻☻♥ ")
        break

    elif (password!=real_password):
        time.sleep(wait_time)
        wait_time*=3
        attemps+=1
    print("after incorrect password ,Retry in ",wait_time,"sec")    


