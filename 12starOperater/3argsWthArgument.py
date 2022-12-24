#args with argument
def multiply_num(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
nums=[1,2,3]
print(multiply_num(nums))# num is list args count list one and multiply with 1 is list
print(multiply_num(*nums))#(*)operater unpack list 

#(*) operator unpack list or tuple 
