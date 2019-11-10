# -*- coding: utf-8 -*
"""Модуль тестов для tasks_two.py"""

import unittest
import tasks_two as tt


class MyTestCase(unittest.TestCase):
    """Класс unit тестов функций tasks_two.py"""

    def test_get_root(self):
        """Тест функции возврата корневого узла"""
        root = tt.get_root('demo.xml')
        self.assertEqual(root.tag, 'data')

    def test_get_list_nodes(self):
        """Тест функции  возврата списка елементов по заданному тегу"""
        list_node = tt.get_list_nodes(tt.get_root('demo.xml'), 'names')
        self.assertEqual(list_node, [])
        list_node = tt.get_list_nodes(tt.get_root('demo.xml'), 'name')
        self.assertEqual(len(list_node), 1)
        self.assertEqual(list_node[0].tag, 'name')
        list_node = tt.get_list_nodes(tt.get_root('demo.xml'), 'languages')
        self.assertEqual(len(list_node), 1)
        self.assertEqual(list_node[0].tag, 'languages')
        list_node = tt.get_list_nodes(tt.get_root('demo.xml'), 'language')
        self.assertEqual(len(list_node), 3)
        self.assertEqual(list_node[0].tag, 'language')
        list_node = tt.get_list_nodes(tt.get_root('demo.xml'), 'pc_item')
        self.assertEqual(len(list_node), 4)
        self.assertEqual(list_node[0].tag, 'pc_item')

    def test_parent_search(self):
        """Тест функции поиска родительского узла"""
        root = tt.parent_search('demo.xml', 'name')
        self.assertEqual(root.tag, 'data')
        root = tt.parent_search('demo.xml', 'pc')
        self.assertEqual(root.tag, 'data')
        root = tt.parent_search('demo.xml', 'pc_item')
        self.assertEqual(root.tag, 'pc')
        root = tt.parent_search('demo.xml', 'pc_i')
        self.assertIsNone(root)

    def test_remove_nodes(self):
        """Тест функции удаления елементов по заданному тегу"""
        list_node = tt.get_list_nodes(tt.get_root('demo.xml'), 'pc_item')
        self.assertEqual(len(list_node), 4)
        root = tt.remove_nodes('demo.xml', 'pc_item')
        list_node = tt.get_list_nodes(root, 'pc_item')
        self.assertEqual(list_node, [])
        root = tt.remove_nodes('demo.xml', 'languages')
        list_language = tt.get_list_nodes(root, 'language')
        list_languages = tt.get_list_nodes(root, 'languages')
        self.assertEqual(len(list_language), 0)
        self.assertEqual(list_languages, [])


if __name__ == '__main__':
    unittest.main()
