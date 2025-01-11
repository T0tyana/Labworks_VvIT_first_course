'''Задание 1: Написание простых функций
Напишите функцию greet, которая принимает имя пользователя в качестве аргумента
и выводит приветствие с этим именем.
Создайте функцию square, которая возвращает квадрат переданного ей числа.
Реализуйте функцию max_of_two, которая принимает два числа в качестве аргументов и возвращает большее из них.
'''

def greet(name):
    print(f'Привет, {name}! Хорошего дня!')

name_in = input("Введите имя: ")
greet(name_in)
print()

def square(number):
    print(number**2)
num = int(input("Введите число: "))
square(num)
print()

def max_of_two(x, y):
    if x > y:
        print("Большое число", x)
    elif y > x:
        print("Большое число", y)
    else:
        print('Числа равны')
one = int(input("Введите первое число: "))
two = int(input("Введите второе число: "))
max_of_two(one, two)


'''Задание 2: Работа с аргументами функций
Напишите функцию describe_person, принимающую имя и возраст человека, 
и печатающую эту информацию в читаемом виде. Сделайте возраст опциональным аргументом со значением по умолчанию 30.
'''
def describe_person(name, age=30):
    print(f'Имя: {name} \nВозраст: {age}')
name_in = input('Введите имя: ')
age_in = input('Введите возраст: ')
if age_in.isdigit() and age_in != '':
    describe_person(name_in, age_in)
else:
    describe_person(name_in)
print()

'''Задание 3: Использование функций для решения алгоритмических задач
Напишите функцию is_prime, которая определяет, является ли число простым, и возвращает True или False соответственно.
'''

def if_prime(number):
    ans = True
    if number <= 1:
        ans = False
        print(ans)
    else:
        for d in range(2, int(number**(1/2)) + 1):
            if number % d == 0:
                ans = False
                break
        print(ans)
num = int(input('Введите число: '))
if_prime(num)
