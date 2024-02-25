#%%
def star(func):
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    return wrapper
def hello():
    print('Hello')
star(hello)()
# %%
# funct is parment parameter 
def ali(funct):
    def wrapper():
        print('*'*10)
        funct()
        print('*'*10)
    return wrapper

def hello():
    print('Hello World!')
ali(hello)()



@ali
def bye():
    print('Are you fine.')
bye()

# %%
