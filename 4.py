x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:
        print('1 coordinate plane')
    elif y < 0:
        print ('4 coordinate plane')
    else:
        print('Unknown')
elif x < 0:
    if y > 0:
        print('2 coordinate plane')
    elif y < 0:
        print('3 coordinate plane')
    else:
        print('Unknown')
else:
    print('Unknown')