companies = ['audi', 'bmw', 'tata', 'toyota', 'mercedes', 'ferrari']
for company in companies:
    if company == 'bmw':
        print(company.upper())
    else:
        print(company.title())
#if statements in python

car = 'Audi'
print(car.lower() == 'audi')
#this doesn't change the value of car but only converts it into lower case for comparison temporarily
#check this by printing car if you want

sum = 1 + 2
if sum == 3:
    print('You are exceptionally brilliant!')
if sum != 3:
    print("You need to brush up on math")

age_1 = 10
age_2 = 20
age_3 = 30
if age_1 == 10 and age_2 == 20:
    print("Both options are correct")

if age_1 == 10 or age_3 == 40:
    print("One option is correct")

if age_1 == 10 and age_3 == 40:
    print("This won't be printed")
else:
    print("One is correct, but no points for you")
#checking the conditions by using 'and' and 'or'

words = ['can', 'python', 'do', 'this']
print('can' in words)
print('not' in words)

word1 = 'amazing'
if 'amazing' not in words:
    print("This is amazing!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
#it is not necessary to use else block. you can omit it and can use elif to be more precise

'''
the if - elif - else chain is powerful, but it’s only appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient and allows you to test for one specific condition. However, sometimes it’s important to check all of 
the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be 
True , and you want to act on every condition that is True
'''

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

alphabets = ['a', 'b', 'c', 'd', 'e']
for alpha in alphabets:
    if alpha == 'c':
        print("Skipping " + alpha)
    else:
        print(alpha + " is the current alphabet")

list_1 = []
if list_1:
    for item in list_1:
        print(item)
else:
    print("The list is empty")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

