# Лабраторная работа 1
## Задача 1
> Напишите программу, которая запрашивает у пользователя ввод числа и выводит на экран все числа от 1 до введенного числа включительно.
```python
num = int(input("Введите число: "))
for i in range(1, num + 1):
    print(i)

print()
```
Запрашиваем у пользователя значение с помощью функции `input()`, функция `int()` приводит значение к целочисленному типу, далее записываем в переменную с именем num. Запускаем цикл `for` и выводим на экран значения, начиная с 1, до введенного занчения включительно, использую функцию `print()`.  Работа цикла `for`: 
`for(start, stop, step)`, где
`start` - начальное значение,
`stop` - конечное значенеие,
`step` - шаг счетчика

## Задача 2
> Напишите программу, которая запрашивает у пользователя ввод 2 чисел и выводит на экран большее из них.
```pyrhon
num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))
if num_one > num_two:
    print('Большое число:', num_one)
elif num_two > num_one:
    print('Большое число:', num_two)
else:
    print('Числа равны')
```
Запрашиваем у пользователя два числа, которые нужно сравнить, и записываем их в переменные num_one и num_two. Далее определяем наибольшее чсило с помощью учловного оператаро (можно использовать встроенную функцию `max()` для упрощения кода)
