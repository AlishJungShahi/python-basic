#%%
class House:
    
    name = 'ramro ghar'
    def __init__(self) -> None:
        print('Hello word')
        self.show()
        
    def __str__(self) -> str:
        return self.name
        
    def show(self):
        print('This is my House')
         
house = House()
print(house)



# %%
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return self.name
        
    def __eq__(self, obj):
        return self.age == obj.age
    
ram = Person('Ram',12)
Shyam = Person('Shyam',11)
print(ram==Shyam)
    

# %%
class Person:
    
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name
    
    def __eq__(self, __value: object) -> bool:
        return self.name == object.name
    
a = Person('Alish', 21)
b = Person('Alish',20)
print(a.name==b.name)


# %%
