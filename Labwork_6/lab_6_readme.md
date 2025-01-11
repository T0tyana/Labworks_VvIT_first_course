# Лабораторная работа №6 
## Задание 1 - Защита данных пользователя
> 1. Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами: имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password).
> 2. Используйте конструктор __init__ для инициализации этих атрибутов.
> 3. Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта.
> 4. Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль текущему паролю аккаунта и возвращает True или False.
> 5. Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его с помощью методов set_password и check_password.
```python
class UserAccount:
    def __init__(self, name, email, password):
        self.username = name
        self.email = email
        self.__password = password

    def _set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password_in):
        return self.__password == password_in


name = input('Введите имя пользователя: ')
email = input('Введите электронную почту: ')
password = input('Введите пароль: ')
obj = UserAccount(name, email, password)
print()

# Замена пароля
new_password = input('Введите новый пароль: ')
obj._set_password(new_password)
print()

# Проверка пароля
print(obj.check_password('haski4'))
print(obj.check_password('Korgi55'))
print()
```

## Задание 2 - Полиморфизм и наследование
> 1. Определите базовый класс Vehicle с атрибутами: make (марка) и model (модель), а также методом get_info(), который возвращает информацию о транспортном средстве.
> 2. Создайте класс Car, наследующий от Vehicle, и добавьте в него атрибут fuel_type (тип топлива). Переопределите метод get_info() таким образом, чтобы он включал информацию о типе топлива.
```python
class Vehicle:
    make = 'Geely'
    model = 'Atlas Pro'

    def get_info(self):
        print(f'Марка машины: {self.make}\nМодель машины: {self.model}')

class Car(Vehicle):
    fuel_type = '95 pulsar'

    def get_info(self):
        print(f"Марка: {self.make}\nМодель: {self.model}\nТип топлива: {self.fuel_type}")

obj_two = Car()
obj_two.get_info()
```
Создаем класс `Vehicle`, который имеет атрибуты `make` и `model`. Создаем класс `Car`, который наследует атрибуты класса `Vehicle` и имеет собственный атрибут `fuel_type`.
