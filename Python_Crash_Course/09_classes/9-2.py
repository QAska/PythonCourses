class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is '" + self.restaurant_name.title() + "'. \nCuisine type: " + self.cuisine_type + '.\n')

    def open(self):
        print('Restaurant is open.')


restaurant_1 = Restaurant('beer without brake', 'beer only')
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant('friends', 'belarussian')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('sweet tooth', 'bakery')
restaurant_3.describe_restaurant()
