number = int(input('Enter your number: '))
if number > 0:
    number /= 10000
    numbers = str(number)
    print(int(numbers[-3:-1]))
"""
this code take the number from user and divide it by 10000 and keep
2 digits of after . then, print those 2numbers

"""
