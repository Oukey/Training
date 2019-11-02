import unittest
import for_xml


class MyTestCase(unittest.TestCase):

    def test_norm(self):
        result = for_xml.get_node_value("demo.xml")
        self.assertEqual(result, [])
        result = for_xml.get_node_value("demo.xml", 1)
        self.assertEqual(result, [])
        result = for_xml.get_node_value("demo.xml", 'pass')
        self.assertEqual(result, [])
        result = for_xml.get_node_value("demo.xml", 'name')
        self.assertEqual(result[0], 'Petya')
        result = for_xml.get_node_value("demo.xml", 'age')
        self.assertEqual(result[0], '23')
        result = for_xml.get_node_value("demo.xml", 'languages')
        self.assertEqual(len(result), 1)
        result = for_xml.get_node_value("demo.xml", 'language')
        self.assertEqual(len(result), 3)
        result = for_xml.get_node_value("demo.xml", 'pc')
        self.assertEqual(len(result), 1)
        result = for_xml.get_node_value("demo.xml", 'pc_item')
        self.assertEqual(len(result), 4)

    def test_norm1(self):
        res = for_xml.count_nodes("demo.xml", 'name')
        self.assertEqual(res, 7)
        res = for_xml.count_nodes("demo.xml", 'age')
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
