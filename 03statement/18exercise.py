# ask user name and count each character 
#name=input("enter your name")
name='prakasah' 
temp_vari=""
for i in range(len(name)):
    if name[i] not in temp_vari:
        temp_vari+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")