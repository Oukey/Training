import xml.etree.ElementTree as ETree


def get_root(xml_file="demo.xml"):
    xml1 = ETree.parse(xml_file)
    return xml1.getroot()


def output_lvl(xml_file):
    '''
    Функция выводит содержание двух уровней вложенности
    (languages и pc), включая название тега, список атрибутов и значение
    '''
    root = get_root(xml_file)
    for elem in root:
        if len(elem) > 0:
            for lvl in elem:
                print(lvl.tag, lvl.get("name"), lvl.text)


def get_node_value(xml_file, tag=None):
    '''Функция формирует список всех значений для конкретного тега если задано его название'''
    root = get_root(xml_file)
    nod_list = []

    def search(el, n_list):
        for i in el:
            if i.tag == tag:
                n_list.append(i.text)
            if len(i) > 0:
                search(i, n_list)

    search(root, nod_list)
    return nod_list


def count_nodes(xml_file, atr):
    '''Функция возвращает количество всех узлов с заданным атрибутом'''
    count = 0
    iter_ = ETree.parse(xml_file).getiterator()
    for elem in iter_:
        if atr in elem.attrib.keys():
            count += 1
    return count


if __name__ == "__main__":
    output_lvl("demo.xml")
    print(get_node_value("demo.xml", 'languages'))
    print(get_node_value("demo.xml", 'language'))
    print(get_node_value("demo.xml", 'pc'))
    print(get_node_value("demo.xml", 'pc_item'))
    print(get_node_value("demo.xml", 'sex'))
    print(count_nodes("demo.xml", 'name'))
