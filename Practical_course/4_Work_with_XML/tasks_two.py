# -*- coding: utf-8 -*-
"""Работа с XML-файлами. Часть вторая"""


def get_list_nodes(xml, tag):
    """
    Функция принимает дерево xml документа и тэг для поиска.
    Формирует и возвращает список всех узлов по заданному тегу
    """
    list_nodes = []
    for element in xml.iter():
        list_nodes += element.findall(tag)
    return list_nodes


def parent_search(xml, node):
    """
    Функция поиска родилеля заданного узла.
    Принимает дерево xml документа и ссылку на узел.
    Возвращает ссылку на родительский узел
    """
    for element in xml.iter():
        if node in element:
            return element
    return None


def remove_nodes(xml, tag):
    """
    Функция удаления всех узлов по заданному тегу
    Принимает дерево xml документа и тег
    """
    new_xml = xml
    for element in new_xml.iter():
        result = element.findall(tag)
        if result:
            for node in result:
                element.remove(node)
    return new_xml


def get_elem(xml, tag):
    """
    Вспомогательная функция возврата элемента по тегу
    """
    for element in xml.iter():
        result = element.findall(tag)
        if result:
            return result[0]
