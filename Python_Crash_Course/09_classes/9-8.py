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


class Privileges:
    def __init__(self):
        self.privileges = [
            'разрешено добавлять сообщения',
            'разрешено удалять пользователей',
            'разрешено банить пользователей'
        ]

    def show_privileges(self):
        print('Пользователю', ', '.join(self.privileges) + '.')


class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


user_1 = Admin('siarhei', 'snob', 33, 'Homel')
user_1.privileges.show_privileges()


