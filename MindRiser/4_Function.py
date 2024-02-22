#%%
def Hello():
    name = input('Enter your name')
    Faculity = input('Enter your Faculity')
    print(f'Dear {name} and your faculity is {Faculity}.')
Hello()


# %%
def hello(name):
    print(f"Dear {name}. We kindly invite you in a metting")
hello('Ram')
hello("Alish")


# %%
def hello(name, Age, sex):
    print(f'Name: {name} \nage: {Age}\nGender: {sex}')
hello('Ram', '19', 'Male')
# %%
# key word argument
def hello(name, Age, sex):
    print(f'Name: {name} \nage: {Age}\nGender: {sex}')
hello(Age='19',name= 'Alish', sex='Male')



# %%
# args
def person(*names):
    for name in names:
        print(f'Hello, {name}')
person('Ram','Shyam','Hari','Alish')

# %%
def person(**names):
    print(names['Name'],names['Age'],names['Gender'])
person(Name = 'Alish', Age = '21', Gender = 'Male')

# %%
def number(n=1):
    print(n)
    if n==10:
        return
    number(n+1)
number()
# %%
def person(n=0):
    print(n)
    if n==10:
        return      
    person(n+1)   
person()

# %%
a = [1,2,3,4,5,6]
a = number()
print(a)

# %%
