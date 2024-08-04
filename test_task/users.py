class UserManager():
    # инициализация класса и методов
    def __init__(self):
        self.users = {}
        self.count = 0

    # добавить юзера и присвоить id
    def addUser(self, name):
        self.count += 1
        user_id = self.count
        self.users[user_id] = name
        return user_id

    # достать юзера по id
    def getUser(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        else: return None

    # удалить юзера и вернуть bool успешности операции
    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        else: return False

    # найти юзера по имени
    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]