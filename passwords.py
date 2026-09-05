from random import *
from os import *

alph = '1234567890-=!@#$%^&*()_+qwertyuiop[]asdfghjkl;zxcvbnm,./йцукенгшщзхъфывапролджэячсмитьбю.'

def create(x):

    s = ''

    for i in range(x):
        s += choice(alph)

    return s

def rb(x):

    s = ''

    for i in range(x):

        s += choice(alph)

    return s

print('Hello, thats program for passwords!\n')

while True:

    print('What do you want?\n')
    print('1) Create pass\n2) Brutforse\n3) Exit')

    w = input()

    if w == '1':

        print('What lenght of pass?\n')

        try:

            le = int(input())

            if le <= 0:

                print('Wrong Value!')                   
                continue

        except ValueError:
            print('Try value')

        print(f'\nHere is your password: {create(le)}')

    elif w == '2':
        print('Bruteforce mode is not implemented yet.')

        car = input()

        if car == '2':
            print('Ohhh... Ok, Ok, brut work, what type you wont?\n')

            ty = input()

            if ty == 'random':

                for i in range(1, 100):

                    le = randint(1, 100)

                    print(rb(le))

            elif ty == 'purposeful':

                print('For defence of anti-brutforse systems, cange delay:\n')

                dela = int(input())

                

    elif w == '3':
        print('Goodbye!')
        break
        
    else:
        print('Unknown command! Please choose 1, 2 or 3.')