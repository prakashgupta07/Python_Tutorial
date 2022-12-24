#function returning function(closures/first class function)
def to_power(x):
        def calc_power(n):
                return x**n
        return calc_power
n=int(input("enter your number"))
x=int(input("enter your number"))
var=to_power(n)
print(var(x))