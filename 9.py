range = int(input('Введите дальность выстрела: '))
if range == 29:
    print("Попал!")
elif range >= 30:
    print('Перелет!')
elif range > 0 and range <= 28:
    print('Недолет!')
else:
    print('Не бей по своим!')