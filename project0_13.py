import math
print('1.Radian to Degree''\n''2.Degree to Radian')
number = int(input('which one do you want to convert? '))
p = math.pi
if number == 1:
    quest = int(input('Enter your number: '))
    result = quest * 180 / p
    print('Radion to Degree is: {}'.format(result))
elif number == 2:
    quest = int(input('Enter your number: '))
    result = quest * p / 180 
    print('Degree to Radion is: {}'.format(result))
