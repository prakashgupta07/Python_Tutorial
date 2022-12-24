# any() and all() function
number1=[2,4,6,8,10]
number2=[1,2,3,4,5,6]
# normal away of check
# it check your number one by one is running your  accourding your program 
# if your number run according to your program it give "true" value every time
# if any number does not run according to program it give "fales" only paticulay place
even1=[]
for i in number1:
        if i%2==0:      # even1.append(i%2==0) you can also use this in place of this
                even1.append(True)
print(even1)

# ############### we check through all() function
# it check your whole number at run according  to your program 
# if it's run it give  "true " value as a output
##if any one number not run it give "false" as a output
print(all([i%2==0 for i in number1]))# it give false value
print(all([i%2==0 for i in number2]))# it give false value

####### any() function
# it check your whole number at run according  to your program 
# if any one number run according to your program ti give "true"as a output
# otherwise its give false value
number3=[2,4,4,6,8]
print(any(i%2!=0 for i in number3))




