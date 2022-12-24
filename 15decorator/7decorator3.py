#decorator part 3
from functools import wraps
def decorator_function(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwarg):
                """this is wrapper function"""
                print("hi this is awesome function")
                return any_function(*args,**kwarg)
        return wrapper_function

@decorator_function
def add(a,b):
        '''this is add function'''
        return a+b

print(add.__doc__)
print(add.__name__)












