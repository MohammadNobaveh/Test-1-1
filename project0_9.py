print('Shapes;')
print('1.Triangle''\n''2.Rectangle''\n''3.Square')
shape = int(input('which shape do you want to calculate? '))
if shape == 1:
    a = input('do you want to calculate area or s? ')
    number = int(input('Now please Enter your number: '))
    if a == 'area':
        area_of_triangle = 3 * number
        print('Area result is: {}'.format(area_of_triangle))
    elif a == 's':
        s_of_triangle = (3 ** 0.5) / 4 * number ** 2
        print('S result is: {}'.format(s_of_triangle))
elif shape == 2:
    b = input('do you want to calculate area or s? ')
    number = list(map(int,input('Now please enter your numbers(length and width): ').split()))
    if b == 'area':
        area_of_rectangle = (number[0] + number[1]) * 2
        print('Area result is: {}'.format(area_of_rectangle))
    elif b == 's':
        s_of_rectangle = number[0] * number[1]
        print('S result is: {}'.format(s_of_rectangle))
elif shape == 3:
    squ = input('do you want to calculate area or s? ')
    number = int(input('Now Enter your number please: '))
    if squ == 'area':
        area_of_square = 4 * number
        print('Area of square: {}'.format(area_of_square))
    elif squ == 's':
        s = number * number 
        print('S result is: {}'.format(s))



