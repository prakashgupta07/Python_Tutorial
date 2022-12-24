#ask user name and print back user name in reverse order
name=input("enter your name")
print(name) 
reverse_name=name[-1::-1]
print(name[-1::-1]) 
print(f"your name is {name} and your reverse name is {reverse_name}") 
print("your name is {} and reverse name is {}".format(name,reverse_name))