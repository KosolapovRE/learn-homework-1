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
    """среднее значение по школе считаю"""
    all_scores = (school_grades[0]['scores'] + school_grades[1]['scores'] + school_grades[2]['scores']) 
    sum_scores = 0
    for element in all_scores:
        sum_scores += element
    average_score = sum_scores / len(all_scores)
    print(average_score)
    """считаю среднее значение по каждому классу"""
    sum_scores_1a = 0
    for element in school_grades[0]['scores']:
        sum_scores_1a += element
    average_score_1a = sum_scores_1a / len(school_grades[0]['scores'])
    print(average_score_1a)

    sum_scores_1b = 0
    for element in school_grades[1]['scores']:
        sum_scores_1b += element
    average_score_1b = sum_scores_1b / len(school_grades[1]['scores'])
    print(average_score_1b)

    sum_scores_2b = 0
    for element in school_grades[2]['scores']:
        sum_scores_2b += element
    average_score_2b = sum_scores_2b / len(school_grades[2]['scores'])
    print(average_score_2b)

    """ написал функцию для подсчета средней оценки по классу, если ее применить, намного меньше кода получится"""

    def average_score_test(scores):
        sum_scores_test = 0
        for element in scores:
            sum_scores_test += element
        average_score_test = sum_scores_test / len(scores)
        return average_score_test

    average_score_1a_test = average_score_test(school_grades[0]['scores'])
    print(average_score_1a_test)

if __name__ == "__main__":
    main()
