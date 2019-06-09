import csv

workers =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]


with open('workers.csv', 'w', encoding='utf-8', newline='') as element:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(element, fields, delimiter=';') 
    writer.writeheader()
    writer.writerows(workers)
