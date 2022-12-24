# python custom exception
# Q-Why custom exceptons?
# 
class NameTooShortError(ValueError):
        pass
def validate(name):
        if len(name)<8:
                raise NameTooShortError("name is too short")

name=input("enter your name")
validate(name)
print(name)