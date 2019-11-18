# -*- coding: utf-8 -*-
"""Пример работы с файлами и каталогами"""

import os.path

# Проверка, существует ли файл методом isfile()
print(os.path.isfile('/bin/bash'))

# Определение размера файла в байтах методом getsize()
print(os.path.getsize('/bin/bash'))
