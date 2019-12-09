# -*- coding: utf-8 -*-
"""Работа с документами doc"""

import os.path

from docx import Document


def string_replacement(file_name, str1, str2):
    """
    Функция получает на вход имя файла(документ Word) и две строки.
    Выполняет замену одной строки на другую.
    При успешной замене возвращает True, иначе False
    """
    if os.path.isfile(file_name):
        document = Document(file_name)
        for per in document.paragraphs:
            if per.text == str1:
                per.text = str2
                document.save(file_name)
                return True
    return False


name_file = 'demo.docx'
str1 = 'A plan paragraph having some bold and some italic'
str2 = 'XXX'


print(string_replacement(name_file, str1, str2))


