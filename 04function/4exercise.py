#define a function which takes number as a input and return greater of two number 
def greater_number(num1,num2):
    if num1>num2:
        return "num1 is greater"
    else:
        return "num2 is greater"
num1=int(input("enter your number 1"))
num2=int(input("enter second number2"))
total=greater_number(num1,num2)
print(total)