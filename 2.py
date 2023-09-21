x1 = int(input('Enter number: '))
x2 = int(input('Enter number: '))
x3 = int(input('Enter number: '))

middle_n = x1
if x1 == x2 or x2 == x3 or x1 == x3:
    middle_n = 'Error'
else:
    if (x2 > x1 and x2 < x3) or (x2 < x1 and x2 > x3):
        middle_n = x2
    elif (x3 > x1 and x3 < x2) or (x3 < x1 and x3 > x2):
        middle_n = x3

print(f'Middle number - {middle_n}')