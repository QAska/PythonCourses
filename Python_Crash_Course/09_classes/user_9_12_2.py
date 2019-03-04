from user_9_12_1 import User


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
