class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print("User's name is", self.first_name.title(), self.last_name.title() + '.',
              'He is', self.age, 'years old.',
              'He is from', self.city + '.')

    def greet_user(self):
        print('Hello,', self.first_name.title() + '!\n')
