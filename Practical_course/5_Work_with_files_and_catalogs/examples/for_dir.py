# -*- coding: utf-8 -*-
"""Пример работы с файлами и каталогами"""

import os.path

# Проверка, существует ли файл без попытки его открытия функцией isfile()
print(os.path.isfile('/bin/bash'))
print(os.path.isfile('1.py'))
print(os.path.isfile('test.txt'))

# Определение размера файла в байтах функцией getsize()
# print(os.path.getsize('test.txt'))

# Переименование файла функцией rename()
# if os.path.isfile('test.txt'):
#     os.rename('test.txt', 'test.txt')

# Перемещение файла функцией rename()
if os.path.isfile('test.txt'):
    os.rename('test.txt', '../test.txt')

#  Удаление файла функцией remove()
# if os.path.isfile('test.txt'):
#     os.remove('test.py')

# Полный путь к файлу при помощи os.path.abspath()
print(os.path.abspath('..1.py'))
