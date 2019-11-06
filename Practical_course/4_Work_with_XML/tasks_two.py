# 1. Написать функциюб которая формирует списко всех узлов по заданному тегу
# независимо от их глубины в XML-документе. На вход функция получает корневой узел

# 2. Написать функцию, которая находит родителя заданного узла

# 3. Написать функцию, которая удаляет все узлы по заданному тегу
# независимо от их глубины в XML-документе

import xml.etree.ElementTree as ETree


def get_root(xml_file="demo.xml"):
    xml2 = ETree.parse(xml_file)
    return xml2.getroot()


def get_list_nodes(rt, tag):
    '''
    Функция формирует и возвращает список всех узлов по заданному тегу
    Функция получает корневой узел
    '''
    list_node = []
    for nod in rt.iter():
        if nod.tag == tag:
            list_node.append(nod)
            # print(nod.tag)
    return list_node


def parent_search(xml_file, node=None):
    '''Функция поиска родителя разанного узла'''
    root = get_root(xml_file)
    for item in root.iter():
        print(item.tag)


def remove_nodes(xml_file, tag):
    '''Функция удаления всех узлов по заданному тегу'''
    root = get_root(xml_file)
    for elem in root.iter():
        item = elem.find(tag)
        elem.remove(item)



'''
xml_file = 'demo.xml'
xml2 = ETree.parse(xml_file)
root = xml2.getroot()
for elem in root.iter():
    # print(elem.tag, elem.text, elem.attrib)
    print(elem.tag)

tag = 'data'
rt = xml2.getroot()
for elem in root.iter():
    item = elem.find(tag)
    if item:
        elem.remove(item)
    # if elem.find(tag):
    #     elem.remove(elem.find(tag))

print('*' * 40)
for elem in rt.iter():
    # print(elem.tag, elem.text, elem.attrib)
    print(elem.tag)

print('*' * 40)
zz = root.find('languages')  #languages
print(zz)




# print(root.tag)
#
# print(get_list_nodes(root, 'name'))
# print(get_list_nodes(root, 'languages'))
# print(get_list_nodes(root, 'language'))
# print('*' * 40)
# l = get_list_nodes(root, 'language')
# l1 = l[1]
# print(type(l1))
#
#
# print('*' * 40)
# print(parent_search(xml_file))

'''