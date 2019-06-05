"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

robot_talk = {
    'Как дела?': 'Круто', 
    'Чем занимаешься?': 'Пишу код на пайтоне', 
    'В субботу куда пойдешь?': 'На занятие в deworkacy Полянка',
    'На яндексе программирование заканчивается?': 'Забудь эту ерунду!'
    }

def ask_user():
    while True:
        try:
            question = input('Что ты хочешь спросить?')
        except KeyboardInterrupt:
            print('Пока!')
            break
        if question == 'Хватит':
            break
        else:
            print(robot_talk.get(question, 'В ответах я ограничен, правильно задавай вопросы!'))
    
                   
ask_user()
