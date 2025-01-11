# Лабораторная работа №5
## Задание 1 - Базовый класс и методы
> Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
> Добавьте метод get_info(), который возвращает информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]".
```python
class Book:

    title = "All for the Game"
    author = "Nora Sakavic"
    year = "2016"
    counter = 0

    def __init__(self):
        Book.counter += 1 # Считаем кол-во экземпляров

    def get_info(self):
        print(f"Название книги: {self.title}\nАтвор: {self.author}\nГод издания: {self.year}.")

obj_one = Book()
obj_one.get_info()
print(obj_one.counter)
obj_two = Book()
print(obj_two.counter)
obj_three = Book()
print(obj_three.counter)
```
Создаем класс `Book` с помощью ключевого слова `class`. Задаем атрибуты класса. Задаем метод `get_info()`. который выводит информацию о книге с помощью функции `print()` и f-строк. Создаем экземпляр класса `obj_one` и выводим информацию о нем.

## Задание 2 - Работа с конструктором
> 1. Определите класс Circle для представления круга.
> 2. Используйте конструктор __init__ для инициализации радиуса круга (radius).
> 3. Добавьте метод get_radius(), который возвращает значение радиуса.
> 4. Добавьте метод set_radius(new_radius), который позволяет изменить радиус круга.
> 5. Создайте объект класса Circle, измените его радиус и выведите новый радиус на экран
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        print(f"Радиус круга - {self.radius}")

    def set_radius(self, new_radius):
        self.radius = new_radius


obj_two = Circle(20)
obj_two.get_radius()
obj_two.set_radius(35)
print(f"Новый радиус круга - {obj_two.radius}")
```
Создаем класс `Circle`. Инициализируем радиус круга с помощью конструктора `__init__`. Добавляем методы `get_radius` и `set_radius`, которые выводят информацию о радиусе круга и изменяют радиус соответственно. 

