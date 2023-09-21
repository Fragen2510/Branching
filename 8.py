year = int(input('Введите год: '))
if year % 100 == 0:
    if year % 400 == 0:
        print('В этом году 366 дней')
    else:
        print('В этом году 365 дней')
elif year % 4 == 0:
    print('В этом году 366 дней')
else:
    print('В этом году 365 дней')
