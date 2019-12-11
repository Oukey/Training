# -*- coding: utf-8 -*-
"""Работа с документами doc"""

import os.path

from docx import Document


def string_replacement(file_name, str1, str2):
    """
    Функция получает на вход имя файла(документ Word) и две строки.
    Выполняет замену первой найденной строки на другую.
    При успешной замене возвращает True, иначе False
    """

    if os.path.isfile(file_name):
        document = Document(file_name)
        # Поиск строки в параграфах
        for per in document.paragraphs:
            if per.text == str1:
                per.text = str2
                document.save(file_name)
                return True
        # Поиск строки в таблицах
        for selected_table in document.tables:
            for selected_row in selected_table.rows:
                for selected_cell in selected_row.cells:
                    if selected_cell.text == str1:
                        selected_cell.text = str2
                        document.save(file_name)
                        return True
    return False
