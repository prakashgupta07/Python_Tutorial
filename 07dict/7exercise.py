# exercise 
#define a function that takes a number (n)
# return a dictionary containing cube of numbers froms 1 to n

def cube_finder(n):
    cube={}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube
n=int(input("enter your  number"))
print(cube_finder(n))