# # Define a list containing different data types
# my_list = ['abcd', 786, 2.23, 'john', 70.2]

# # Accessing and printing individual characters of the first element in the list
# first_element = my_list[3]
# for char in first_element:
#     print(char)

# name = 'ALish Shahi'
# first_name = name[:5]
# print(first_name)

# print(name[6:11])

# #%%
# print("Hello world")
# # %%


#%%
Name = 'Kamal Bahadur Shahi'
mid_name = Name[5:12]
print(mid_name)
# %%
colors = ["Green", "Blue", "Yello"]
colors.append("Red")
colors.insert(2, 'Pink')
colors.pop(3)
colors[1] = 'dark gray'
print(colors)
# %%
country_code = [('Nepal','Np'),('India','Id'),('China','Cn')]
print(country_code)
country_code.append(('Pakistan','Pk'))
print(country_code)


# %%

colors = {'red','red','pink','yellow','pink'}
print(colors)
colors[1] = set('oraneg')
# %%
d1 = {'name': 'Alish', 'age': 23, 'Class':10}
d1['age']
# %%
name = input('Enter your name')
di.insert(name)
# %%
d1 = [
    {'name': 'Alish','age': 23, 'class': 'BIT'},
    {'name': 'Santosh','age': 19, 'class': 'BHM'},
    {'name': 'Hari','age': 20, 'class': 'IT','Time':20}]

for i in d1:
    print(i.get('name',''))
# %%
