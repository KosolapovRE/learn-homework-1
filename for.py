"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_grades = [
    {'school_class': '1a', 'scores': [3, 4, 4, 2, 3, 5, 3, 2, 5]}, 
    {'school_class': '1b', 'scores': [5, 5, 4, 4, 3, 4, 5]}, 
    {'school_class': '2b', 'scores': [3, 3, 3, 2, 5]}
    ]
    scores_1a = school_grades[0]['scores'] 
    total = 0
    for element in scores_1a:
        total += element
    average_score = total / len(scores_1a)
    print(average_score)
    scores_1b = school_grades[1]['scores']
    total = 0
    for element in scores_1b:
        total += element
    average_score = total / len(scores_1b)
    print(scores_1b)
        
    pass
    
if __name__ == "__main__":
    main()
