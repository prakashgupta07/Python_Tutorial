# rise error
def add(a,b):
        if type(a)== int and type(b)==int:
                return a+b
        raise TypeError(" you are passing worng data type to function")
print(add("a","b"))