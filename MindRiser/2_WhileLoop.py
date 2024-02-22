#%%
# intro of while loop
n = 1
while n<=10:
    print(f"{n}.Hello")
    n = n+1
print("This is how loops work")


# %%
# how to use condition in loop
n = 1
while n<=10:
    print(f"{n}.Hello")
    if n==5:
        break
    n = n+1
print("This is how loops work")



# %%
# usnig range
number = range(10)
print(number, type(number))


# %%
# how to use range
number = range(1, 20)
xx = list(number)
print(list(number))
print(type(xx))


 # %%
#  print even number using loop
number = range(0,10,2)
print(list(number))


# %%
# print even number using while loop
n = 0
while n<=10:
    print(n)
    n = n+2
    
    
# %%
# print even number using while loop
n = 0
while n<=10:
    if n%2==0:
        print(n,"Even number")
    n = n+1


# %%
# check member is in or not
a = [1,2,3,4,5]
print(1 in a)
# %%
for a in range(10):
    print(a)
# %%
inder = 1
a = ['apple', 'orange', 'kiwi']
for inder, a in enumerate(a):
    
     print(f"{inder+1}. {a}")
    
# %%
def print_even_numbers(start, end):
    print(f"Even numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
start_interval = int(input("Enter the start of the interval: "))
end_interval = int(input("Enter the end of the interval: "))

print_even_numbers(start_interval, end_interval)
 
20
# %%
def number(start,end):
    print(f'Even number between {start} and {end} are: ')
    for num in range(start,end+1):
        if num %2==0:
            print(num, end=" ")
start = int(input('Enter your start number you want'))
end = int(input('Enter your end number you want'))
number(start,end)

20# %%

# %%
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("Enter the length of the password: "))
random_password = generate_random_password(password_length)
print("Randomly generated password:", random_password)

# %%
import random
import string

def ramdom_pw(length):
    characters = string.ascii_letters +string.digits +string.punctuation+string.ascii_lowercase+string.ascii_uppercase
    pasword = ''.join(random.choice(characters) for i in range (length))
    return pasword
password_length = int(input('Enter the length of password'))
random_pw = generate_random_password(password_length)
print("Random generated password is:", ramdom_pw)


# %%
import math

def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius.
    
    Arguments:
    radius -- the radius of the circle
    
    Returns:
    The area of the circle.
    """
    return math.pi * radius ** 2

# Example usage
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print("The area of the circle is:", area)

# %%
