#decorator practice
from functools import wraps
def print_function_data(function):
        @wraps(function)
        def wrapper_function(*args,**kwargs):
                print(f"you are calling {function.__name__} function")
                print(f"{function.__doc__}")
                return function(*args,**kwargs)
        return wrapper_function
@print_function_data
def add(a,b):
        '''this function take two numbers as arguments and return their sum'''
        return a+b
print(add(3,4))
# add=print_function_data(add)
# print(add(3,4))