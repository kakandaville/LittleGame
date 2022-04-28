from random import *
from os import system
import time

num = randint(1,101)



while True:


    n = int(input("\nВведите чисельцо, от одного до 100\n"))
    if 0 < n < 101:
        pass

    else:
        continue

    if n == num:

        print('УГАДАЛ УРААА')

        print('Дотвиданя')


        input()
        exit(0)




    elif n < num:

        print('Хрен то там! Слишком мало!')

    elif n > num:

        print('Ага, конечно! Слишком много!')

    # a = input('\nЕщё попыточку? д/н\n')
    #
    # if a == 'д':
    #     pass
    #
    # elif a == 'н':
    #     exit(0)






