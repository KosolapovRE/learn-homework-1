
def main():
    if __name__ == "__main__": 
        main()


years = input('Привет дорогой друг, напиши свой возраст и я угадаю, чем ты занимаешься!')
def what_you_do(years):
    try:
        years = int(years)
    except (ValueError, TypeError):
        return 'Вы неправильно ввели возраст'
    
    if years <= 0:
        return 'Ты еще не родился!'
    elif years <= 6:
        return 'Ты ходишь в детский сад!'
    elif years <= 17:
        return 'Ты учишься в школе!'
    elif years <= 23:
        return 'Ты учишься в ВУЗе!'
    elif years <= 65:
        return 'Ты ходишь на работу!'
    elif years <= 100:
        return 'После 65 лет ты не можешь работать, ты пенсионер!'
    elif years > 100:
        return 'Так долго люди не живут, ты иноплянетянин!'


answer = what_you_do(years)
print(answer)

