#%%
class grandparents():
    house = 'Nice House'

class father(grandparents):
    car = 'Lambo'
    
class son(father):
    console = 'ps5'
    
Son = son()
print(Son.car)
print(Son.house)
print(isinstance(son,object))
print(isinstance(son,father))


# %%
# method overhide

class grandfather:
    house = 'nice house'
    
class father(grandfather):
    car = 'lambo'
    
    
    def __init__(self):
        print('I am father')
        
class son(father):
    console = 'ps5'
    
Son = son()
    


# %%
# method overhide

class grandfather:
    house = 'nice house'
    
class father(grandfather):
    car = 'lambo'
    
    
    def __init__(self):
        print('I am father')
        
class son(father):
    console = 'ps5'
    
    def __init__(self):
        print('I am son')
        super().__init__() #\\to print all
    
Son = son()


    

# %%
class information:
    
    def __init__(self,name,age,password) -> None:
        self.name = name
        self._age = age
        self.__password = password
        
Information = information('Alish',21,'1234@')

print(Information.name)
print(Information._age)     #'''run only this file'''
print(Information.__password)  #'''for sefty'''



# %%
class person:
    def __init__(self,name,age,password) -> None:
        self.name = name
        self.age = age
        self.password = password
        
    def set_password(self):
        return self.set__password
    
    def get_password(self):
        return self.get_password
    
Person = person('Alish',21,'@alish')
print(Person.password)


# %%


