# Write a Python program to check if a year is a leap year. 
# A leap year is either divisible by 4 but not divisible by 100, 
# or it is divisible by 400


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
