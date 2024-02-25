Letter = '''Dear <|NAME|>,
Greeting from ABC coding house. I am happy to tell you about your selection
you are selected!
Have a great day ahead.
Thanks and regards,
dare: <|DATE|>
'''

name = input("Enter your name\n")
date = input("ENter today date\n")
Letter = Letter.replace("<|NAME|>", name)
Letter = Letter.replace("<|DATE|>", date)
print(Letter)


# eg 2
# alish = "dear name. conguralation for selected. date"

# NAME = input("Enter your name")
# DATE = input("Enter today date")

# alish = alish.replace("name", NAME)
# alish = alish.replace("date", DATE)

# print(alish)