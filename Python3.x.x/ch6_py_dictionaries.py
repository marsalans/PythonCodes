man = {'height': '5ft', 'age': 34, 'mks': 24}
print(man['height'])
print(man['mks'])
#this is called a dictionary. It is a collection of key value pairs

#you can dynamically add new key values

print(man)
man['sex'] = 'male'
man['country'] = 'india'
print(man)

man2 = {}
#this creates an empty dictionary

man['country'] = 'usa'
print(man['country'])
#the above example shows how to change a value of a dictionary

if man['age'] == 18:
    to_add = 2
elif man['age'] == 24:
    to_add = 5
elif man['age'] == 30:
    to_add = 8
else:
    to_add = 0
    print("You too old")

man['age'] = man['age'] + to_add
print(man['age'])

del man['mks']
print(man)
#deleting or removing information

salaries = {
    'engg': 10000,
    'dr': 20000,
    'lawyer': 5000,
    'architect': 8000,
}

for key, value in salaries.items():
    print("\nOccupation: " + str(key))
    print("Salary: " + str(value))
#you can use any names instead of key and value since they are variables. i have used str() since my orginal text is int
#you can use string instead of int as i have done above


for occ in salaries.keys():
    print(occ.title())
#note that i have use salaries.keys() instead of salaries.items(). this is used to iterate only either keys or value in a dictionary

for sal in salaries.values():
    # print("\n" + str(sal))
    print(sal)

friends = ['engg', 'lawyer']
for occ in salaries.keys():
    print(occ.title())
    if occ in friends:
        print(" Hi " + occ.title() + ", I see your salary is " + str(salaries[occ]) + "!")
    if 'driver' not in salaries:
        print("Why is driver not given any salary?")
#this is an amazing example which shows how you can use everything you've learned so far

print("\n")

for occ in sorted(salaries.keys()):
    print(occ.title() + " is capitalized and ordered")

alien_0 = {'color': 'red', 'points': 20}
alien_1 = {'color': 'green', 'points': 35}
alien_2 = {'color': 'blue', 'points': 15}

alien = [alien_0, alien_1, alien_2]

print("\n")

for item in alien:
    print(item)

aliens = []

for alien_no in range(30):
    new_alien = {'color': 'violet', 'points': 50}
    aliens.append(new_alien)

count = 0
for alien in aliens[:5]:
    print(alien)
    count = count + 1

print("\n")
print("Total no. of aliens: " + str(len(aliens)))
print("Printed " + str(count) + " aliens")

pizza = {

    'crust': 'thicc',
    #lmao
    'toppings': ['mushrooms', 'cheese', 'veggies']
}

print("You ordered a " + pizza['crust'] + " crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print(topping.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username) 
    full_name = user_info['first'] + " " + user_info['last'] 
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
#study the above example. why to use serinfo['last] and not username['last]

#got it. user_info stores the values inside aeinstein and mcurie i.e. 'first', 'last' and 'location' while username stores aeinstein and mcurie


print("\n")

