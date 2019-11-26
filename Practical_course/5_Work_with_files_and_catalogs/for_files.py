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


def dir_removal(name):
    """
    Функция удаления каталога со всеми файлами если в нем нет подкаталогов
    При удачном удалении возвращает True, иначе False
    """
    files = data_lists(name)[0]
    catalogs = data_lists(name)[1]
    if os.path.isdir(name) and len(catalogs) == 0:
        if len(files) > 0:
            os.chdir(name)  # переход в каталог для удаления вложенных файлов
            for file in files:
                os.remove(file)
        os.chdir('../')  # возврат в "рабочий" каталог
        os.rmdir(name)
        return True
    return False
