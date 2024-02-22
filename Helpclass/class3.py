#%%
def main():
    name = str(input('Enter your name'))
    grade = str(input('Enter your grade'))
    print(name)
    print(grade)
main()
# %%

#%%
def ali():
    length = float(input('Enter the length of rectangle'))
    width = float(input('Enter the width of rectangle'))
    area = length * width
    print(area)
    
ali()
# %%


def time():
    timeInsecond = int(input('Enter a time in second: '))
    hours = timeInsecond// 3600
    remaining_second = timeInsecond % 3600
    minutes = remaining_second // 60
    secoond = remaining_second % 60
    
    print(f"{timeInsecond} secoond = {hours}hours, {minutes}minutes, {secoond}sec,")
    
time()

# %%

def shop():
    item1 = float(input('Enter your first item'))
    item2 = float(input('Enter your second item'))
    item3 = float(input('Enter your third item'))
    print('A program to find the cost for three purchased items')
    
    total = item1+item2+item3
    discount = total * 0.10
    netProfit = total-discount
    print(f"The total item is = RM.{total}\n 10% of discount = RM.{discount}\n Net cost = Rm.{netProfit}")
    
    # print('The total iteam is:',total)
shop()

# %%
def shop():
    item1 = float(input('Enter your first item'))
    item2 = float(input('Enter your second item'))
    item3 = float(input('Enter your third item'))
    print('A program to find the cost for three purchased items')
    
    total = item1+item2+item3
    discount = total * 0.10
    netProfit = total-discount
    
    print("cost of three item = RM{:.2f}".format(total))
    print("10% of discount = RM{:.3f}".format(discount))
    print("Net cost = RM{:.3f}".format(netProfit))
     
shop()

# %%
userName = str(input('Enter your ursename: '))
password = str(input('Enter your password: '))
if userName == "Admin":
    if password == "Password":
        print('Login successful! Welcome, admin')
        
    elif password == "12345":
        print('Week password, Please reset your password')
    else:
        print('Incorrect password')

else:
    if userName == "guest":
        if password == "guest":
            print('Login successful! Welcome, guest')
            
        else:
            print('Incorrect Password')
            
    else:
        print('unknown user. Please try again')
# %%
name = input('Enter your name')
email = input('Enter your email')
password = input('Enter your password')

if name == "":
    print('Name cannot be empty')
    
else:
    if "@" not in email:
        print("Invalid email")
    elif len(password)<8:
        print('Ar least your password has minimum 8 character')
    else:
        print('Login successful!')

        
# %%
i = 1
while i<6:
    print(i)
    i+=1

# %%


for x in "Apple":
    print(x)

#%%
for x in range(2,6):
    print(x)
#%%   
for x in range(1,30,3):
    print(x)
#%%
fruits = ['apple','banana','orange']
fruits.pop(2)
print(fruits)
for apple in fruits:
    print(apple)
    
#%%   
    