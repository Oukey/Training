import xml.etree.ElementTree as ETree


def get_root(xml_file="demo.xml"):
    xml1 = ETree.parse(xml_file)
    return xml1.getroot()


def output_lvl(xml_file):
    '''
    Функция выводит содержание двух уровней вложенновсти
    (languages и pc), включая название тега, список атрибутов и значение
    '''
    root = get_root(xml_file)
    for elem in root:
        if len(elem) > 0:
            for lvl in elem:
                print(lvl.tag, lvl.attrib['name'], lvl.text)


def get_node_value(xml_file, tag=None):
    '''Функция формирует список всех значений для конкретного тэга если задано его название'''
    root = get_root(xml_file)
    nod_list = []
    for elem in root:
        if elem.tag == tag:
            if len(elem) == 0:
                nod_list.append(elem.text)
            else:
                for lvl in elem:
                    # nod_list.append(lvl.get("name") + ' ' + lvl.text)
                    nod_list.append(lvl.text)
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
    # print(get_node_value("demo.xml", 'languages'))
    # print(get_node_value("demo.xml", 'pc'))
    # print(get_node_value("demo.xml", 'sex'))
    print(count_nodes("demo.xml", 'name'))
