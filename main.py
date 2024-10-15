# Система управления учетными записями пользователей
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять
# пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    # Общий список пользователей для всех экземпляров класса User
    users = []

    def __init__(self, id, name, permission):
        self.id = id
        self.name = name
        self.permission = permission

class Admin(User):
    # users = []  # Общий  пользователей для всех экземпляров класса Admin

    def __init__(self, id, name, permission):
        super().__init__(id, name, permission)

    def __add_user(self, id, name, permission):
        if permission.lower() in ['user', 'admin']:
            user = (id, name, permission.lower())
            Admin.users.append(user)
            print(f"Пользователь id={id}, имя={name} c правом доступа '{permission}' добавлен")
        else:
            print("Ошибка: неверные права доступа")
            print(f"Отклонено добавление пользователя id={id}, имя={name} c правом доступа '{permission}'")


    def __remove_user(self, id):
        users_to_remove = [user for user in Admin.users if user[0] == id]
        for user in users_to_remove:
            Admin.users.remove(user)
            print(f"Пользователь (id={user[0]}, имя={user[1]}) c правами доступа '{user[2]}' удалён")

    def set_user(self, id, name, permission):
        self.__add_user(id, name, permission)

    def get_remove(self, id):
        self.__remove_user(id)

# Использование класса Admin
admin = Admin(0, 'superadmin', 'admin')
# admin.__add_user(1, 'vasya', 'user') # Приводит к ошибке, т.к. нет доступа к функции __add_user
admin.set_user(1, 'vasya', 'user')
admin.set_user(5, 'serg', 'Админ')  # Приводит к ошибке, т.к. не правильно указано право доступа
admin.set_user(2, 'masha', 'User')
admin.set_user(2, 'sega', 'user')   # Специально добавлен пользователь с уже существующим ID=2, т.к. проверка на уникальность ID не производится
admin.set_user(3, 'vera', 'admin')
admin.get_remove(2)  # Удалит обоих пользователей с ID=2
