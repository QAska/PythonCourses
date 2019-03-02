class User():
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


user_1 = User('siarhei', 'snob', 34, 'Gomel')
user_2 = User('ivan', 'ivanov', 24, 'Minsk')
user_3 = User('petr', 'petrov', 44, 'SF')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
