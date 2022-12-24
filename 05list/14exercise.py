# define a function which will take list containing numbar as input 
# and return list cointaining squre of every element 
def squre_number(num):
    squre=[]
    for i in  num:
        squre.append(i*i)
    return squre 
number=list(range(1,11))

print(squre_number(number))