#kwargs(keywords arguments)
# **kwargs(double star operator)

# kwargs as a parameter
def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))

    for k,v in kwargs.items():
        print(f"{k}:{v}") 
# dictionary unpacking
d={'name':'prakash','age':24}
func(**d)
#func(first_name ='prakash', last_name ='gupta')