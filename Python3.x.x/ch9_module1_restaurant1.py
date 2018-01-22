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
