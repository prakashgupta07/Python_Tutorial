#ask user number like 23456 
#calculate the sum of digit 4+5+2+3+
n=input("enter a number in digit")
total=0
for i in range(len(n)):
    total+=int(n[i]) 
print(total)