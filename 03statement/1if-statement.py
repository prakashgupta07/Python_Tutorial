#if statement  
name,age=input("enter your name and age" ).split(",")
age=int(age) 
if age>=14:
    print(f"hello {name} your age is {age} and you are above 14")