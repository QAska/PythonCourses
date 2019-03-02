class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name.title() + '. \nCuisine type is ' + self.cuisine_type + '.')

    def open(self):
        print('Restaurant is open.')

    def reading_number_served(self):
        print('Served number is ' + str(self.number_served) + '.')

    def set_number_reserved(self, amount):
        self.number_served = amount

    def increment_number_reserved(self, number):
        self.number_served += number


restaurant = Restaurant('friends', 'belarussian')
# restaurant.number_served = 10

restaurant.describe_restaurant()
restaurant.open()
restaurant.reading_number_served()
restaurant.set_number_reserved(10)
restaurant.increment_number_reserved(5)
restaurant.reading_number_served()
