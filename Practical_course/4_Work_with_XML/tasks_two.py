# -*- coding: utf-8 -*-

# 1. Написать функциюб которая формирует списко всех узлов по заданному тегу
# независимо от их глубины в XML-документе. На вход функция получает корневой узел

# 2. Написать функцию, которая находит родителя заданного узла

# 3. Написать функцию, которая удаляет все узлы по заданному тегу
# независимо от их глубины в XML-документе

import xml.etree.ElementTree as ETree


def get_root(xml_file="demo.xml"):
    xml2 = ETree.parse(xml_file)
    return xml2.getroot()


def get_list_nodes(root, tag):
    """
    Функция формирует и возвращает список всех узлов по заданному тегу
    Функция получает корневой узел
    """
    list_node = []
    for elem in root.iter():
        # list_node = elem.findall(tag)
        if elem.tag == tag:
            list_node.append(elem)
    return list_node


def parent_search(xml_file, tag):
    """Функция поиска родителя занного узла"""
    root = get_root(xml_file)
    for elem in root.iter():
        if elem.findall(tag):
            return elem


def remove_nodes(xml_file, tag):
    """ Функция удаления всех узлов по заданному тегу """
    root = get_root(xml_file)
    for elem in root.iter():
        result = elem.findall(tag)
        for node in result:
            elem.remove(node)
    return root


# def output_elem(xml_file):
#     root = get_root(xml_file)
#     for elem in root.iter():
#         print(elem.tag)

tag = 'pc_item'
root = get_root('demo.xml')
for el in root.iter():
    print(el)

root = remove_nodes('demo.xml', tag)
# for elem in root.iter():
#     res = elem.findall(tag)
#     for el in res:
#         elem.remove(el)


print('-' * 50)
for el in root.iter():
    print(el)

# item = root.find(tag)
# print('!!!--{}--!!!'.format(item))


l = []

for e in l:
    print('+')
