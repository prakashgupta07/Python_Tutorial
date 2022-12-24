# define function to make first letter capital in list 
def capital(l,**kwargs):
    if kwargs.get('reverse_str')== True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

name=['prakash','gupta']
print(capital(name, reverse_str=True ))