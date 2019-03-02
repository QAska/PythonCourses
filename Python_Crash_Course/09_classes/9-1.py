class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name.title() + '. \nCuisine type is ' + self.cuisine_type + '.')

    def open(self):
        print('Restaurant is open.')


restaurant = Restaurant('friends', 'belarussian')
restaurant.describe_restaurant()
restaurant.open()
