# -*- coding: utf-8 -*-
"""Работа с XML-файлами. Часть вторая"""

import xml.etree.ElementTree as ETRee

'''
Задания
1. Напишите функцию, которая формирует список всех узлов по заданному тегу независимо от их глубины в XML-документе.
На вход функция получает корневой узел.
2. Напишите функцию, которая находит родителя заданного узла.
3. Напишите функцию, которая удаляет все узлы по заданному тегу независимо от их глубины в XML-документе.
4. Для трёх предыдущих функций напишите тесты.
'''


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


XML2 = ETRee.parse('demo.xml')
print(XML2)
print(type(XML2))
for elem in XML2.iter():
    print(elem)
print('___________1___________')
TAG = 'data'
print(get_list_nodes(XML2, TAG))
print('___________2___________')
NODE = get_elem(XML2, TAG)
print(NODE)
print(parent_search(XML2, NODE))
print('___________3___________')
remove_nodes(XML2, TAG)
# print(remove_nodes(XML2, TAG))
XML2 = remove_nodes(XML2, TAG)
for elem in XML2.iter():
    print(elem)
