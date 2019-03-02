class User():
    def __init__(self, first_name, last_name, age, city, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = login_attempts

    def describe_user(self):
        print("User's name is", self.first_name.title(), self.last_name.title() + '.',
              'He is', self.age, 'years old.',
              'He is from', self.city + '.')

    def greet_user(self):
        print('Hello,', self.first_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('siarhei', 'snob', 34, 'Gomel', 0)

user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
