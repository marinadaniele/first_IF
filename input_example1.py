# name = input("What is your name?")
# age = input("How old are you?")
# age = int(age)
# birth_year = 2023- age
#
# print("OMG", name, "you are", age, "years old so you were born in", birth_year)
#
# try:
#     age1 = int(input(" What is your age1? "))
# except ValueError:
#     print(" I am sorry but that is not a valid number")
# else:
#     print("Your age is", age1)
#
# try:
#     age_p1 = int(input("What is your age player 1?"))
#     age_p2 = int(input("What is your age player 2?"))
#     res = age_p1/age_p2
#
# except ZeroDivisionError:
#     print("I am sorry, but you cannot divide by zero")
#
# except:
#     print("I am sorry, but something went wrong")
#
# else:
#     print("Player 1 is older than Player 2 by a factor of", res)

import random
drinks = ["beer", "wine", "whiskey", "campari", "tequila", "vodka", "rum", "gin tonic", "aperol", "sangria"]

try:
    age = int(input("How old are you?"))
    country = input("Where do you live?")

except ValueError:
    print("I'm sorry but your age is not a valid number")

# else:
#     if age < 0:
#         print("I'm sorry but your age cannot be a negative number")
#     elif age > 130:
#         print("I'm sorry but your age cannot be greater than 130")
#
#     print("Thank you for playing, you are", age, "years old" )

# or join two exceptions
else:
    if age < 0 or age > 130:
        print("I'm sorry but your age cannot be a negative number or greater than 130")

    elif age < 18:
        print("I'm sorry, but you're not old enough to play this drinking game anywhere in the world")
    elif age < 21 and country == "US" or country == "USA":
        print("I'm sorry, you're too young to be playing this game in the USA")
    else:
        drink = random.choice(drinks)
        print("Take a shot of", drink, "thank you for playing, you are", age, "years old, so you can play this game in your country." )
