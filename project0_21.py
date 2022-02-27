user_string = input('Enter your word to check it\'s palindrome: ')
rev = reversed(user_string)
if list(user_string) == list(rev):
    print('palindrome')
else:
    print('NOT palindrome')