alien_0={'colour':'green', 'points':5}
print(alien_0['colour'])
print(alien_0['points'])
new_points=alien_0['points']
print(f"You have won {str(new_points)} points!")
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#Modifying values in a dictionary
alien_0={'colour':'green'}
alien_0['colour']='yellow'
print(f"The alien's colour is now {alien_0['colour']}.")

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original x_position: {str(alien_0['x_position'])}")

if alien_0['speed'] == 'slow':
    x_increment=1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print(f"New x_position: {str(alien_0['x_position'])}.")

alien_0={'colour':'green', 'points':5}
del alien_0['points']
print(alien_0)

favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'js',
    }
print(f"Denzel's favourite language is,{favourite_languages['denzel'].title()}.")

for k,v in favourite_languages.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")
    print(f"{k.title()}'s favouite language is {v.title()}")

friend={'first_name':'Jamila','last_name':'Suleiman','age':20,'city':'Mombasa'}
print(friend)

glosary={
    'print':'python prints a message',
    'for':'is a loop',
    'in':'looks for specific value in a list',
    'if':'condition',
    'else':'condition',
    }
print(f"Print: {glosary['print']}.\n")
print(f"For: {glosary['for']}.\n")
print(f"In: {glosary['in']}.\n")
print(f"If: {glosary['if']}.\n")
print(f"Else: {glosary['else']}.")

alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points', 'No point Value.')
print(point_value)

#LOOPING THROUGH A DICTIONARIES
user_0={
    'username':'joelvegas',
    'first_name':'Effy',
    'last_name':'Owuor',
    }

for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'js',
    }
for name in favourite_languages:
    print(f"\n{name.title()}")

favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'js',
    }

friends=['shali','joel']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language=favourite_languages[name].title()
        print(f"{name.title()}, I see you love {language.title()}")


favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'js',
    }

if 'Macquine' not in favourite_languages.keys():
    print("Macquine please take your poll.\n")

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thankyou for taking the poll.")


favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'python',
    }

print("The following languages have been mentioned:")
for language in sorted(favourite_languages.values()):
    print(language)#NOTICE PYTHON HAS BEEN REPEATED TWICE NOW USE THE SET() METHOD TO FIX THIS

favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'python',
    }

print("\n The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language)

glosary={
    'print':'python prints a message',
    'for':'is a loop',
    'in':'looks for specific value in a list',
    'if':'condition',
    'else':'condition',
    }

for k,v in sorted(glosary.items()):
    print(f"\n{k.title()}: {v}")

Rivers={
    'nile':'egypt',
    'congo':'congo',
    'mississippi':'usa',
    'amazon':'brazil',
    }

country=['usa']
for k,v in sorted(Rivers.items()):
    if v in country:
        v=v.upper()
    else:
        v=v.title()

    print(f"\nRiver {k.title()} is the longest river in {v}")

Rivers={
    'nile':'egypt',
    'congo':'congo',
    'mississippi':'usa',
    'amazon':'brazil',
    }

for k in sorted(Rivers.keys()):
    print(k.title())
for v in sorted(Rivers.values()):
    if v in country:
            v=v.upper()
    else:
            v=v.title()

    print(v)

favourite_languages={
    'denzel':'python',
    'shali':'c++',
    'joel':'c',
    'phinky':'python',
    }

pollers=['bravin','shali','fidel','joel']

for k in sorted(pollers):
    if k in favourite_languages.keys():
        print(f"\nI'm sorry {k.title()}, you had already taken the poll, thankyou for your contribution.")
    else:
        print(f"\nHi {k.title()}, you can take your poll now. ")


#NESTING
alien_0={'color':'green', 'points':5}
alien_1={'color':'yellow', 'ponts':10}
alien_2={'color':'red', 'ponts':15}

aliens=[alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)