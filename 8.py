year = int(input('Введите год: '))
if year % 4 == 0:
    if year // 100 and year % 400 == 0:
        print('В этом году 366 дней')
    else:
        print("Этот год невисокосный")
else:
    print("Этот год невисокосный")
