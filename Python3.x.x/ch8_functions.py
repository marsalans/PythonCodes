import ch8_module1 as chm1
from ch8_module2 import print_nos
from ch8_module3 import sum_of_nos_and_making_it_a_long_title as son


'''

def greeting(name):
    print("Hello " + name + ". Welcome!")

u_name = input("Type your name: ")
greeting(u_name)
greeting("Noah")
#showing how to pass parameter(s) to the function


def ret_name(f_name, l_name):
    full_name = f_name + ' ' + l_name
    return full_name.title()

o_name = ret_name('james', 'hardy')
print("The full name is " + o_name + " .")


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
#copied this example which states that you don't have to have the middle name

'''


'''

def ret_dict(f_name, l_name):
    person = {
        'first': f_name,
        'last': l_name
    }
    return person

full_name = ret_dict('James', 'Morgan')
print(full_name)

def greet(name):
    for sample in name:
        msg = "Hello " + sample.title() + " "
        print(msg)

names = ['james', 'jolie', 'uma']
greet(names)
#passing a list as a parameter


concept_designs = ['iphone design', 'samsung design', 'oneplus design']
final_designs = []

while concept_designs:
    current_design = concept_designs.pop()
    print(current_design.title() + " popped")
    final_designs.append(current_design)

for model in final_designs:
    print(model.title())

def list_toppings(*toppings):
    for topping in toppings:
        print("-" + topping.title())

#the asterix is used when we are unsure how many parameters will be passed
#the passed parameters are then converted or stored as a list

#try the above loop using while loop

list_toppings('pepperoni')
list_toppings('cheese', 'mushrooms')


'''



'''

def s_toppings(size, *toppings):
    print("Pizza size is: " + str(size) + " and the toppings are: ")
    for top in toppings:
        print("-" + top.title())

s_toppings(12, 'mushrooms')
s_toppings(16, 'cheese', 'pepperoni', 'chilly')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
    location='princeton',
    field='physics')
print(user_profile)

#double asterisk is used when we are unsure what kind of information will be passed
#this converts it into a dictionary


'''


#ch8_module1.print_dict()

#commented the above function call to demonstrate the as functionality of module1
#to use the functions of another python file, you need to import using the import keyword during the start of the script
# it and then use the functions in the above fashion

print_nos()
#you can even import specific functions from a module and directly call the function as stated above

son()
#if the name of the function you are importing is long, you can use 'as' keyword to shorten it

chm1.print_dict()
#similarly you can use 'as' keyword to shorten module names too


#to import all functions of a module, use '*'



