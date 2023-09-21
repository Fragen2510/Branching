x1 = int(input('Enter number: '))
x2 = int(input('Enter number: '))
x3 = int(input('Enter number: '))
max_n = x1
min_n = x1
if x2 > x1 and x2 > x3:
    max_n = x2
elif x3 > x1 and x3 > x2:
    max_n = x3

if x2 < x1 and x2 < x3:
    min_n = x2
elif x3 < x1 and x3 < x2:
    min_n = x3
print (f'max number - {max_n}\nmin number - {min_n}')