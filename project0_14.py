numbers = list(map(int,input('Enter your numbers to check: ').split()))
if numbers[0] + numbers[1] > numbers[2] and numbers[2] + numbers[1] > numbers[0] and numbers[2] + numbers[0] > numbers[1]:
    print('Yes! you can make a triangle!!!!!')
else:
    print('Nope! you can\'t make it!!')
"""
the condition of making triangle is that the sum of 2 sides 
are bigger than the other one!

"""
