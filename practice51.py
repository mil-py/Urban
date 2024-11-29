class User:
    def __init__(self, username, password, password_confirm):
        self.name = username
        if password == password_confirm:
            self.password = password
class Database:
    def __init__(self):
        self.data = {}
    def add_user(self,username, password):
        self.data[username] = password

if __name__ == '__main__':
    database= Database()
    user = User(input('введите имя '),input('введите пароль '),input('повторите пароль '))

    database.add_user(user.name, user.password)
