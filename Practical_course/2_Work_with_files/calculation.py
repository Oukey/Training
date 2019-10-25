import random


def sum_file(name):
    '''
    Функция принимает номер файла
    Возвращает сумму чисел в файле
    '''
    sum = 0
    check = True
    lines = 0
    with open(str(name) + '.txt', 'rt') as file:
        line = file.readline()
        while line != '':
            try:
                sum += int(line.rstrip())
                lines += 1
                line = file.readline()
            except ValueError:
                check = False
                break
        if lines == 3 and check is True:
            return sum
        else:
            print("В файле '{}.txt' не корректные данные".format(name))


def res_files(n, m):
    '''
    Функция получает два числа от 1 до 10, открывает одноименные файлы
    И возвращает сумму чисел в двух файлах
    '''
    try:
        return sum_file(n) + sum_file(m)
    except TypeError:
        print('Не корректные данные')


rand_num_1 = 11
# rand_num_1 = random.randint(1, 10)
rand_num_2 = 12
# rand_num_2 = random.randint(1, 10)
print("Сумма чисел в файле '{}.txt' == {}".format(rand_num_1, sum_file(rand_num_1)))
print("Сумма чисел в файле '{}.txt' == {}".format(rand_num_2, sum_file(rand_num_2)))
print("Сумма чисел в двух выбранных файлах == {}".format(res_files(rand_num_1, rand_num_2)))

