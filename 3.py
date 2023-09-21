x1 = int(input('Enter bigger number: '))
x2 = int(input('Enter smaller number: '))

remainder = x1 % x2

if remainder == 0:
    print('The number x2 is a multiple of x1')
else:
    print (f'The number x2 is not a multiple of x1\nremainder - {remainder}')