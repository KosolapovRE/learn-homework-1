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

def main():
    first_str = input('Напишите что нибудь - ')
    second_str = input('Напишите еще что нибудь - ')
    first_str = first_str.lower().replace(' ', '')
    second_str = second_str.lower().replace(' ', '')
    if second_str =='learn':
        if len(first_str) != len(second_str):
            print(3)
        else:
            print(1)
    else:
            if len(first_str) == len(second_str):
                print(1)
            else:
                if len(first_str) > len(second_str):
                    print(2)
                else:
                    print('Вторая строка больше первой!')
    
        
            
        
        
  

    
if __name__ == "__main__":
    main()
