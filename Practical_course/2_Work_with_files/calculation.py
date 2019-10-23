import random


def sum_file(name):
    '''
    Функция принимает номер файла
    Возвращает сумму чисел в файле
    '''
    sum = 0
    with open(str(name) + '.txt', 'rt') as file:
        line = file.readline()
        while line != '':
            sum += int(line.rstrip())
            line = file.readline()
    return sum


def res_files(n, m):
    '''
    Функция получает два числа от 1 до 10, открывает одноименные файлы
    И возвращает сумму чисел в двух файлах
    '''
    return sum_file(n) + sum_file(m)


rand_num_1 = random.randint(1, 10)
rand_num_2 = random.randint(1, 10)
print("Сумма чисел в файле '{}.txt' == {}".format(rand_num_1, sum_file(rand_num_1)))
print("Сумма чисел в файле '{}.txt' == {}".format(rand_num_2, sum_file(rand_num_2)))
print("Сумма чисел в двух выбранных файлах == {}".format(res_files(rand_num_1, rand_num_2)))
