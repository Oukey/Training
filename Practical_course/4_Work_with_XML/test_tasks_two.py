# -*- coding: utf-8 -*
"""Модуль тестов для tasks_two.py"""

import unittest
import tasks_two as tt
import xml.etree.ElementTree as ETRee


class MyTestCase(unittest.TestCase):
    """Класс unit тестов функций tasks_two.py"""

    def test_get_list_nodes(self):
        """Тест функции  возврата списка елементов по заданному тегу"""
        xml = ETRee.parse('demo.xml')
        list_node = tt.get_list_nodes(xml, 'names')
        self.assertEqual(list_node, [])
        list_node = tt.get_list_nodes(xml, 'name')
        self.assertEqual(len(list_node), 1)
        self.assertEqual(list_node[0].tag, 'name')
        list_node = tt.get_list_nodes(xml, 'languages')
        self.assertEqual(len(list_node), 1)
        self.assertEqual(list_node[0].tag, 'languages')
        list_node = tt.get_list_nodes(xml, 'language')
        self.assertEqual(len(list_node), 3)
        self.assertEqual(list_node[0].tag, 'language')
        list_node = tt.get_list_nodes(xml, 'pc_item')
        self.assertEqual(len(list_node), 4)
        self.assertEqual(list_node[0].tag, 'pc_item')

    def test_parent_search(self):
        """Тест функции поиска родительского узла"""
        xml = ETRee.parse('demo.xml')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'name'))
        self.assertEqual(parent.tag, 'data')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'age'))
        self.assertEqual(parent.tag, 'data')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'sex'))
        self.assertEqual(parent.tag, 'data')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'pc'))
        self.assertEqual(parent.tag, 'data')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'pc_item'))
        self.assertEqual(parent.tag, 'pc')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'languages'))
        self.assertEqual(parent.tag, 'data')
        parent = tt.parent_search(xml, tt.get_elem(xml, 'language'))
        self.assertEqual(parent.tag, 'languages')
        # Поиск родителя отсутствующего узла
        parent = tt.parent_search(xml, tt.get_elem(xml, 'missing'))
        self.assertIsNone(parent)
        parent = tt.parent_search(xml, tt.get_elem(xml, 'data'))
        self.assertIsNone(parent)


    def test_remove_nodes(self):
        """Тест функции удаления елементов по заданному тегу"""
        xml = ETRee.parse('demo.xml')
        list_node = tt.get_list_nodes(xml, 'pc_item')
        self.assertEqual(len(list_node), 4)
        len_ = 0
        for _ in xml.iter():
            len_ += 1
        self.assertEqual(len_, 13)
        test_missing = tt.remove_nodes(xml, 'missing')
        len_xml = 0
        for _ in test_missing.iter():
            len_xml += 1
        self.assertEqual(len_xml, 13)

        new_xml = tt.remove_nodes(xml, 'pc_item')
        list_node = tt.get_list_nodes(new_xml, 'pc_item')
        self.assertEqual(list_node, [])
        len_xml = 0
        for _ in new_xml.iter():
            len_xml += 1
        self.assertEqual(len_xml, 9)

        new_xml1 = tt.remove_nodes(new_xml, 'languages')
        list_language = tt.get_list_nodes(new_xml1, 'language')
        list_languages = tt.get_list_nodes(new_xml1, 'languages')
        self.assertEqual(len(list_language), 0)
        self.assertEqual(list_languages, [])
        len_xml1 = 0
        for _ in new_xml1.iter():
            len_xml1 += 1
        self.assertEqual(len_xml1, 5)


if __name__ == '__main__':
    unittest.main()
