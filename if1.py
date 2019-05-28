def main():
    years = input('Привет дорогой друг, напиши свой возраст и я угадаю, чем ты занимаешься!')
    years = int(years)
    if years <= 6:
        print('Ты ходишь в детский сад!')
    elif years <= 17:
        print('Ты учишься в школе!')
    elif years <= 23:
        print('Ты учишься в ВУЗе!')
    elif years <= 65:
        print('Ты ходишь на работу!')
    elif years <= 100:
        print('После 65 лет ты не можешь работать, ты пенсионер!')
    elif years > 100:
        print('Так долго люди не живут, ты иноплянетянин!')
    return print(years)
    
if __name__ == "__main__": 
    main()