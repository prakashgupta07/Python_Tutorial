#function returning function
def outer_fun():
        def inner_fun():
                print("inner func")
        return inner_fun

# var=outer_fun()
# var()

def outer_fun2(msg):
        def inner_fun2():
                print(f"message is {msg}")
        return inner_fun2
var=outer_fun2("hi there  !!")
var()