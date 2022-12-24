# function two value
#from typing import MutableMapping


def function(int1,int2):
    add=int1+int2
    multi=int1*int2
    return add,multi

print(function(4,5)) # it gives value in tuple
add,multi=function(4,5) 
print(add)
print(multi)