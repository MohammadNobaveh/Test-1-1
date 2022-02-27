print('F or C')
degree = input('Enter Tempreture to convert: Fahrenheit or celsius: ')
# if user put f or F degree convert to fahrenheit / if put c or C degree convert to celsius
tempre = int(input('Enter temperature: '))
if degree == 'f' or degree == 'F':
    f = (tempre * 1.8) + 32
    print(f'result to fahrenheit is: {f}')
elif degree == 'c' or degree == 'C':
    c = 5/9 * (tempre - 32)
    print(f'result to celsius is: {c}')
