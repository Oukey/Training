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
    for nod in root.iter():
        if nod.tag == tag:
            list_node.append(nod)
    return list_node


def parent_search(xml_file, tag):
    """Функция поиска родителя разанного узла"""
    root = get_root(xml_file)
    for elem in root.iter():
        if elem.findall(tag):
            return elem


def remove_nodes(xml_file, tag):
    """ Функция удаления всех узлов по заданному тегу """
    pass


# def output_elem(xml_file):
#     root = get_root(xml_file)
#     for elem in root.iter():
#         print(elem.tag)

