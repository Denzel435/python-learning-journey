names=['fidel','effy','jeremy']
print(names[0].title())
print(names[1].title())
print(names[2].title())

names=['fidel','effy','jeremy']
for name in names:
    print("What is your favourite music " + name.title() + ".")

fav_machines=['kawasaki','bmw','mercedes']
print("I would like to one day own a " + fav_machines[0].title() + ".")
print("What a luxury is the " + fav_machines[1].upper() + " GTR8.")
print("The prestige of owning a " + fav_machines[2].title() + " is what motivates me more to own it.")

guests=['mom','shali','thanos','grace']
for guest in guests:
    print("Hello " + guest.title() + ", I am inviting you for dinner, hope you'll show up.")
print("It's okay " + guests[1].title() + " if you can't make it, I'll really miss you.")
guests.pop(1)
guests.insert(1,'Zendaya')
print(guests)
for guest in guests:
    print("Hello " + guest.title() + ", I am inviting you to a dinner, hope to see you.")
print("Hello guys, I've just found a bigger dining table.")
guests.insert(0,'Faith')
guests.insert(2,'Debra')
guests.append('Jaldesa')
for guest in guests:
    print("Hello " + guest.title() + ", I'm inviting you for a dinner, hope to see you there.")
print("Ooh shoot! I can only invite two people since there has been a delay in the delivery of the new table.I'm so sorry.")


cars=['bmw','audi','maserati','tesla']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("\n Here's the original list:")
print(cars)
print("\n Here's the sorted list:")
print(sorted(cars))
print("\n Here's the original list again:")
print(cars)
cars.reverse()
print(cars)

destinations=['miami','paris','germany','china','london']
print(destinations)
print(sorted(destinations))
print(destinations)
for destination in destinations:
    print(destination)
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort()
print(destinations)
destinations.sort(reverse=True)
print(destinations)

guests=['mom','shali','thanos','grace']
len(guests)


#Working with lists
natures=['mountains','stars','thunder','birds']
for nature in natures:
    print(nature.title())
    print(nature.title() + " and Revelation alike testify of God's love!")

print("\nNature and Revelation alike tesify of God's love! \n                                _Steps to Christ")

professions=('neurosurgeon','engineer','data scientist','ML engineer')
for profession in professions:
    print("Denzel your hard work has made you an exceptional " + profession.title())

print("\nI am now pursuing Engineering, whilst studying python. By God's grace I will graduate with a first class honors with ML skills then work for five years and then persue Neurosurgery!")


big_cats=['lion','tiger','leopard','jaguar']
for big_cat in big_cats:
    print("A " + big_cat.title() + " is one of the most dangerous cats alive.")
print("\nEvery cat in this list can kill a grown man in just minutes.")

#Making numerical lists
for value in range(1,6):
    print(value)

numbers=list(range(1,6))
print(numbers)
even_numbers=list(range(4,20,5))#first number is where it starts then middle is the maximum it could get then the last value tells python to add it to the first value until maximum
print(even_numbers)
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares=[value**2 for value in range(1,11)]
print(squares)

for value in range(1,21):
    print(value)

for value in range(1,21,2):
    print (value)
for value in range(3,31,3):
    print(value)
cubes=[value**3 for value in range(1,11)]
print(cubes)
for cube in cubes:
    print(cube)

#Working with part of a list
crushies=['shali','winfred','grace']
print(crushies[:2])
print(crushies[0].title() + " you don't know it yet but I really love you!")
crushies.append('mitchelle')
print(crushies)
print(crushies[1:3])#first number is the index second tells python to count from first item
print(crushies[-3:])

print("\nHere are my first three crushies progressively since primary school:")
crushies.reverse()
for crushy in crushies[:3]:
    print(crushy.title())

my_foods=['pilau','chapati','eggs','beans']
friend_foods=my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('kachumbari')
friend_foods.append('biriani')
print(my_foods)
print(friend_foods)

#tuples
dimensions=(200,50)
print(dimensions[:])
for dimension in dimensions:
    print(dimension)
print("This are the original dimensions.")

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print(my_foods)
print("\nThe first three Items inmy list are:")
for my_food in my_foods[:3]:
    print(my_food.title())
print("\nThree items from the list are:")
for my_food in my_foods[1:4]:
    print(my_food.title())
print("\nThe last three items in my list are:" )
for my_food in my_foods[-3:]:
    print(my_food.title())

#Tuples
delicacies=('sparghetti','pizza','octopus','tea')
for delicacy in delicacies:
    print(delicacy.title())
delicacies=('sparghetti','chapati','sushi','tea')
print("\nModified delicacies:")
for delicacy in delicacies:
    print(delicacy.title())