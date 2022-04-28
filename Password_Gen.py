from random import *


def generate_password(len1, char1):
    passw = ''

    for i in range(len1):
        passw+= choice(char1)

    return passw

chars = ''

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

n = int(input('Hello, mr Credo! So how much passwords do you want?\n'))

leng= int(input('And how long will it be?\n'))

dig = input('Are we using digits? y/n\n')

if dig == 'y':
    chars +=digits

uc = input('Are we upper case letters? y/n\n')

if uc == 'y':
    chars +=uppercase_letters

lc = input('Are we lowercase numbers? y/n\n')

if lc == 'y':
    chars +=lowercase_letters

symb = input('Are we using different symbols? y/n\n')

if symb == 'y':
    chars +=punctuation


for i in range(n):
    print('Ваш пароль:', generate_password(leng,chars))