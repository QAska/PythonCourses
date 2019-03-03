class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name.title() + '. \nCuisine type is ' + self.cuisine_type + '.')

    def open(self):
        print('Restaurant', self.restaurant_name, 'is open.')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        print('Sorts of food:', ', '.join(self.flavors) + '.')


restaurant = IceCreamStand('IceWorld', 'Icecream', ['cold', 'hot'])
restaurant.describe_restaurant()
restaurant.open()
restaurant.describe_flavors()
