# function with parameters
def fun(name='unknown',age='24'):
    print(name)
    print(age)

fun()# defult parameters if you not pass any things it pass parameter as a answer
fun('prakash',25)# if you pass argument while calling function  then it give argument as aanswer 

#parameter
#*args
# defult parameters
# **kwargs
def fun(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
fun('prakash', 1,2,3,a=1,b=2 )