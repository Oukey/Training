# -*- coding: utf-8 -*-
"""Работа с файлами и каталогами"""

import os.path


def data_lists(name=None):
    """Функция возвращает список всех файлов и список всех каталогов в текущей директории"""
    list_files = []
    list_catalogs = []
    if not name:
        name = '.'
    if not os.path.isdir(name):
        return [], []
    for root, dirs, files in os.walk(name):
        list_files += files
        list_catalogs += dirs
    return list_files, list_catalogs


def dir_removal(name_dir):
    """
    Функция удаления каталога со всеми файлами если в нем нет подкаталогов
    При удачном удалении возвращает True, иначе False
    """
    if os.path.isdir(name_dir):  # Если указанный каталог существует
        list_dir = os.listdir(name_dir)
        if len(list_dir) == 0:  # Если указанный каталог пустой
            os.rmdir(name_dir)
            return True
        else:  # Если есть вложенные элементы
            os.chdir(name_dir)  # Переход в каталог
            for elem in list_dir:  # Проверка на наличие подкаталогов
                if os.path.isdir(elem):
                    return False
            # Если нет подкаталогов происходит удаление вложенных файлов
            for elem in list_dir:
                os.remove(elem)
            os.chdir('../')  # возврат в рабочий каталог для удаления каталога
            os.rmdir(name_dir)
            return True
    else:
        return False
