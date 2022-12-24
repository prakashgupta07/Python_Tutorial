#ask user for name 
# example- "prakash gupta"
# print count of each words 
name=input("enter your name")
i=0
temp_variable=""
while i<len(name): 
    if name[i] not in temp_variable:
        temp_variable+=name[i]
        print(f"{name[i]}:{name.count(name[i])}") 
    i+=1