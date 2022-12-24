# any() and all() function
def sum(*args):
        if all(type(arg)==int or type(arg)==float for arg in args):
                total=0
                for i in args:
                        total+=i
        return total

print(sum(1,2,3,4,5))
print(sum(1,2,3,4.0,'prakash'))