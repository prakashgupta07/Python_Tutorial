# make flexible function 
# * operator 
#* args
# add function without * operator 
# def add(a,b):
#     return a+b

# print(add(2,3,4)) 

# add function with *operator
def add(*args):
    total=0
    for i in args:
        total+=i
    return total


print(add(1,2,3))