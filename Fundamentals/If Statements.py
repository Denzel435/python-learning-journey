cars=['bmw','mercedes','audi','subaru']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 <= 21:
    print("You can't drink now!")

requested_toppings=['mushrooms','letuce','cheese']
if 'mushrooms' in requested_toppings:
    print("I'd like mushrooms please!")

banned_users=['alex','enock','collins']
user='quavo'

if user not in banned_users:
    print(user.title() + " you can destroy your life now!")

age=12

if age < 5:
    price=0
elif age < 18:
    price=500
else:
    price=1000

print("Your admission cost is " + str(price) + "/=")

#Testing multiple conditions
print(requested_toppings)

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms!")
if 'letuce' in requested_toppings:
    print("Adding letuce!")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni!")

print("\nFinnished making your pizza!")

alien_colors=['green','red','yellow']

if 'green' in alien_colors:
    print("Congradulation, you have earned 5 points!")
else:
    print("Congradulations, you have earned 10 points!")
if'brown' in alien_colors:
    print("Congradulations, you have earned 80 points!")
else:
    print("Congradulations, you have earned 10 points!")

alien_colors=['yellow','green','red']
if 'blue' in alien_colors:
    print("You have earned 5 points!")
elif 'violet' in alien_colors:
    print("You have earned 10 points!")
else:
    print("You have earned 15 points!")

age=20

if age < 2 :
    print("You are a baby.")
elif age < 4:
    print("You are toddler.")
elif age < 13:
    print("Still a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You're an adult.")
elif age > 65:
    print("Elder.")

favourite_fruits=['pineapples','mangoes','oranges']
if 'pineapples' in favourite_fruits:
    print("This my most favourite fruit.")
if 'oranges' in favourite_fruits:
    print("This comes at the second of the list.")
if 'mangoes' in favourite_fruits:
    print("This closes the my list of favourite fruits.")

#Using if statements in lists:Checking for special items
requested_toppings=['mushrooms','extra cheese','green peppers']

for requested_topping in requested_toppings:
    print("Adding { requested_topping}.")

print("\nFinishing making your pizza.")

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry, we're out of green pepper.")
    else:
        print(f"Adding { requested_topping}.")

print("\nFinished making your pizza.")

#Checking that a list is not empty                  ,
requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plane pizza?")

#Using multiple lists
available_toppings=['mushroom','fish','kachumbari','extra cheese','green peppers']
requested_toppings=['kachumbari','tumeric','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry {requested_topping} has finished.")
print("\n Finished making your pizza")

usernames=['admin','denzel435','phinky168','joelvegas','klausenock']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like the status report?")
    else:
        print(f"Hello {username.title()}, thankyou for logging in again.")

usernames=[]

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like the status report?")
        else:
            print(f"Hello {username.title()}, thankyou for logging in again.")
else:
    print("\nWe really need to find some users.")

current_users=['admin','denzel435','joelvegas','klausenock','ni fidel','phinky168']
new_users=['admin','denzel435','docc','leo_og','olilla']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"You'll need to enter a new username {new_user.title()}, because the username is currently in use!")
    else:
        print(f"This username, {new_user.title()}, is available please proceed.")

numbers=[1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
