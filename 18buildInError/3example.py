# rise error example 1
#NotImplementedError/abstract method(are work in java)

class Animal:
        def __init__(self,name):
                self.name=name
        def sound(self):
                raise NotImplementedError("you have not inplemented in subclass")
        
class Dog(Animal):
        def __init__(self,name,breed):
                super().__init__(name)
                self.breed=breed
        
        def sound(self):
            return 'bhow bhow'

class Cat(Animal):
        def __init__(self,name,breed):
                super().__init__(name)
                self.breed=breed
        def sound(self):
                return 'meao meao'
dog=Dog("bonny","pug")
cat=Cat("pussy","italian")
print(cat.sound())