#string vs list
# string    -string are immutable
s="prakash"
s.title() 
print(s) #onece you defind  you can't change again
t=s.title() # change and store in other variable
print(t)
# list are mutable
l=['apple','banana','grapes']
l.pop()
print(l)# you can your original string 
l.append('mango')
print(l)
