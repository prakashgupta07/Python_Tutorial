import time
#list vs generator
# memory uses ,time 
#when to use list , when to use generator 
t1=time.time()
#l=[i**2 for i in range(10000000)]
l=(i**2 for i in range(10000000))
t2=time.time()
time_taken=(t2-t1)
print(time_taken)
#l=(i**2 for i in range(100000000))
