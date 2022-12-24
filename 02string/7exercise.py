#Ask user to input three number and you have to print average of three namber using string formating and try to take  
# all three comma seprate in one line  
a,b,c=input("enter three number number a,b and c").split(",") 
average=((int(a)+int(b)+int(c))//3)  
print(average)
print("average of{},{}and{}is{}".format(a,b,c,str(average)))

print(f"average of {a},{b},and{c} is {average}")