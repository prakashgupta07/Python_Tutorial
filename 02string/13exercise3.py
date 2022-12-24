#take input comma seperated name and char ,and count the char?
name,char=input("enter your name and char").split(",") 
name=name.lower() 
char=char.lower()
print("your length of your name is{}".format(len(name)))
print(f"your length of your name is {len(name)}") 
print(f"character count {name.count(char)}") 
print("character count {}".format(name.lower().count(char.lower())))