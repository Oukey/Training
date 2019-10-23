import random


def create_files():
    ''' Функция создания десяти файлов с тремя случайными числами в каждой строке '''
    for i in range(1, 11):
        with open(str(i) + '.txt', 'wt') as f:
            for _ in range(3):
                f.write(str(random.randint(1, 100)) + '\n')


create_files()
