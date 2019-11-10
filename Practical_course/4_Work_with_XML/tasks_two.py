# -*- coding: utf-8 -*-
"""Работа с XML-файлами. Часть вторая"""

import xml.etree.ElementTree as ETree


def get_root(xml_file="demo.xml"):
    """Функция вщзвращает корневой узел"""
    xml2 = ETree.parse(xml_file)
    return xml2.getroot()


def get_list_nodes(root, tag):
    """
    Функция формирует и возвращает список всех узлов по заданному тегу
    Функция получает корневой узел
    """
    list_node = []
    for elem in root.iter():
        list_node += elem.findall(tag)
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
