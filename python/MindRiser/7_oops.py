# class House:
#     window = 10
#     color = 'Red'
#     door = '5'
#     Address = 'Kathmandu'
    
# Hari_house = House()
# print('Hari house has',Hari_house.window, 'window')

# Alish_house = House()
# print('Alish house color is',Alish_house.color, 'color')





# class House:
#     window = 11
#     color = 'red'
#     door = 1
    
#     def set_window(self, window):  # Corrected method name to set_window
#         self.window = window
        
#     def get_window(self):
#         return self.window
    
# ram_house = House()  # Corrected instantiation with parentheses
# ram_house.set_window(12)  # Corrected method call
# print(ram_house.get_window())  # Corrected method call





# class Burger:
    
#     def bun(self):
#         print('Bun')
#         return self
#     def chees(self):
#         print('chees')
#         return self
#     def patty(self):
#         print('patty')
#         return self
# burger = Burger()
# burger.bun().chees().patty().bun()
# # print(burger.bun())
#%%
database = [
    {
    'name': 'Alish',
    'password': '1122'
    },
    {
    'name': 'Anjil',
    'password': '2233'
    },
    {
    'name': 'Alina',
    'password': '3344'
    },
    {
    'name': 'Sita',
    'password': '4455'
    }
   
]
print(database)
for i in range(2):
    name = input('Enter your name: ')
    password = input('Enter your password: ')


    user={
        'name':name,
        'password':password
    }
    
    database.append(user)
print(database)
# %%
