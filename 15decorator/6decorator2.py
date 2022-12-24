#decorator part 2
def decorator_function(any_function):
        def wrapper_function(*args,**kwarg):
                print("hi this is awesome function")
                return any_function(*args,**kwarg)
        return wrapper_function
# def func1(a):
#         print(f'this is function 1 {a}')
# func1=decorator_function(func1)
# func1(7)
#@decorator_function #this is shortcut
def add(a,b):
        return a+b
add=decorator_function(add)
print(add(2,3))