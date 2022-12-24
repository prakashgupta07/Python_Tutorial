#define greatest 
# find greatest between three number 
def greatest(a,b,c):
    if a>b and a>c:
        return " a is greater"
    elif b>a and b>c:
        return "b is greater "
    else:
        return "c is greater"
a=int(input("enter your number"))
b=int(input("enter your number"))
c=int(input("enter your number"))
total=greatest(a,b,c)
print(total)