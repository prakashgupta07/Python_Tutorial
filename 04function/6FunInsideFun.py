#function inside function
def greater(a,b):
    if a>b:
        return a 
    return b 

def new_greater(a,b,c):
    return greater(greater(a,b),c)
total=new_greater(10,20,30)
print(total)