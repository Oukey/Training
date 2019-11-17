# -*- coding: utf-8 -*-
"""Работа с XML-файлами. Часть вторая"""

import xml.etree.ElementTree as ETree


def get_root(xml_file="demo.xml"):
    """Функция возвращает корневой узел"""
    xml2 = ETree.parse(xml_file)
    return xml2.getroot()


def get_elem(tag):
    """ """
    s = 0
    for node in root.iter():
        return node.findall(tag)
    # return s


# def get_list_nodes(root, tag):
def get_list_nodes(root, tag):
    """
    Функция формирует и возвращает список всех узлов по заданному тегу
    Функция получает корневой узел
    """
    list_node = []
    for elem in root.iter():
        list_node += elem.findall(tag)
    return list_node


# def parent_search(xml_file, element):
# def parent_search(xml_file, tag):
def parent_search(element):
    """Функция поиска родителя заданного узла"""
    for node in root.iter():
        if element in node:
            return node

    # root = get_root(xml_file)
    # for elem in root.iter():
    #     if elem.findall(tag):
    #         return elem


def remove_nodes(xml_file, tag):
    """ Функция удаления всех узлов по заданному тегу """
    root = get_root(xml_file)
    for elem in root.iter():
        result = elem.findall(tag)
        for node in result:
            elem.remove(node)
    return root


root = get_root('demo.xml')
root1 = get_root('demo.xml')
elem_list = []
elem_list1 = []
for elem in root.iter():
    elem_list.append(elem)
    # print(elem.attrib)
for elem in root1.iter():
    elem_list1.append(elem)
print(elem_list)
print(elem_list1)
print('!!!' * 10, elem_list[1].find('.//'))

print(elem_list1[3] in elem_list[0])
print(type(elem_list[1]))
print('+' * 40)
print(get_elem('pc_item'))
print('+' * 40)
# print(parent_search('demo.xml', elem_list[2]))
# print(parent_search(elem_list[2]))
print('+' * 40)
print(parent_search(get_elem('language')))


tree = ETree.parse('demo.xml')
root = tree.getroot()
l1 = []
l2 = []
for elem in tree.iter():
    l1.append(elem)
for node in root.iter():
    l2.append(node)
print(l1)
print(l2)
print(l1[2].tag)
# print(ETree.dump(l1[1]))
