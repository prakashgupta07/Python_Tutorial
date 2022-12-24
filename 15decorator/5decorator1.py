#decorator intro
def decorator_function(any_function):
        def wrapper_function():
                print("hi this is awesome function")
                any_function()
        return wrapper_function
@decorator_function
def func1():
        print("this is func1")
func1()

# var=decorator_function(func1)
# var()
@decorator_function
def fun2():
        print("this is function 2")
fun2()
