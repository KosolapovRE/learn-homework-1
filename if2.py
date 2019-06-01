"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""

first_str = input('Напишите что нибудь - ')
second_str = input('Напишите еще что нибудь - ')

def main(first_str, second_str):
    first_str = first_str.lower().replace(' ', '')
    second_str = second_str.lower().replace(' ', '')
    if second_str =='learn':
        if len(first_str) != len(second_str):
            return '3'
        else:
            return '1'
    else:
        if len(first_str) == len(second_str):
            return '1'
        else:
            if len(first_str) > len(second_str):
                return '2'
            else:
                return 'Вторая строка больше первой!'

   

