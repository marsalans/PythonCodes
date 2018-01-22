import ch9_module1_restaurant1 as ch9
from random import randint
#importing a module from python standard library

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

        '''
        usually classes have upper case latter as the first letter
        2 leading and trailing underscores are used for class methods so as to not confuse with the functions
        the 1st parameter must always be self since when the python later calls the method, the method call will automatically pass the self argument
        Every method call associated with a class automatically passes self , which
        is a reference to the instance itself; it gives the individual instance access to
        the attributes and methods in the class. When we make an instance of Dog ,
        Python will call the __init__() method from the Dog class. We’ll pass Dog()
        a name and an age as arguments; self is passed automatically, so we don’t
        need to pass it. Whenever we want to make an instance from the Dog class,
        we’ll provide values for only the last two parameters, name and age .
        '''


'''

my_dog = Dog('rocky', 5)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
#this is an instance of a class

my_dog.roll_over()
my_dog.sit()
#after creating an instance of a class you can use it to call any method of the class


class Restaurant():
    def __init__(self, res_name, cuis_type):
        self.res_name = res_name
        self.cuis_type = cuis_type

    def display_info(self):
        print("Restaurant name is " + self.res_name.title() + " and has " + self.cuis_type.title() + " cuisine")

    def is_open(self):
        print("Restaurant " + self.res_name.title() + " is now open")

res1 = Restaurant('marriot', 'french')

res2 = Restaurant('Meridian', 'thai')

res1.display_info()
res1.is_open()

res2.display_info()
res2.is_open()


'''



class Car():
    def __init__(self, company_name, year, model_name):
        self.company_name = company_name
        self.year = year
        self.model_name = model_name
        self.odometer_reading = 0

    def display_info(self):
        print(self.company_name.title() + ' ' + self.model_name.title() + ' ' + str(self.year))

    def change_reading(self, odometer_reading):
        self.odometer_reading += odometer_reading

    def read_reading(self):
        print("Miles: " + str(self.odometer_reading))

car1 = Car('BMW', '2015', 'X5')
car1.display_info()
car1.change_reading(250)
car1.read_reading()

car1.change_reading(300)
car1.read_reading()

#increases the miles after calling the function


class ElectricCar(Car):
    def __init__(self, company_name, year, model_name):
        super().__init__(company_name, year, model_name)
    #the arguments passed in the init should be same as that of the super class

    def battery_size(self, model):
        if (model == 'e'):
            self.model_name = model
            self.battery = 70
        elif (model == 'x'):
            self.model_name = model
            self.battery = 90
        else:
            self.model_name = model
            self.battery = 80
        print("Model " + self.model_name.title() + " has " + str(self.battery) + "kWh battery")

        #after putting the else block, the code doesn't work for other model name eg. farady as i have called later. look into this later

'''
ElectricCar is the child class of Car. to do this, parent class must appear before ElectricCar and the name of the parent class must be included in the parenthesis
the super functions helps to make a connection between super class and the sub class. the init method tells the python to call the method from parent class which gives the child class
all its attributes

'''

ecar1 = ElectricCar('tesla', 2017, 'e')
ecar1.display_info()
ecar1.battery_size('e')
ecar1.battery_size('x')
ecar1.battery_size('faraday')   

'''

class NewRestaurant():
    def __init__(self, res_name, cuis_type):
        self.res_name = res_name
        self.cuis_type = cuis_type

    def display_info(self):
        print("Restaurant name is " + self.res_name.title() +
              " and has " + self.cuis_type.title() + " cuisine")

    def is_open(self):
        print("Restaurant " + self.res_name.title() + " is now open")


class IceCreamStand(NewRestaurant):
    def __init__(self, res_name, cuis_type):
        super().__init__(res_name, cuis_type)

    def display_flavour(self, flavour):
        self.flavour = flavour
        print('The flavour is: ' + self.flavour.title())

ics = IceCreamStand("Jumbo's", 'french')
ics.display_info()
ics2 = IceCreamStand("Barkley", 'thai')
flav = input("Which flavour do you like? ")
ics2.display_flavour(flav)

'''


#similar to how you import functions from a module, you can import classes too.
#to demonstrate this, i have commented the above code and written it in another module and then imported it


ics = ch9.IceCreamStand("Jumbo's", 'french')
ics.display_info()
ics2 = ch9.IceCreamStand("Barkley", 'thai')
flav = input("Which flavour do you like? ")
ics2.display_flavour(flav)

print(randint(1, 23))


class Dice():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self, side):
        self.side = side
        print(self.side)

side = randint(1, 6)

die1 = Dice()
die1.roll_die(side)

