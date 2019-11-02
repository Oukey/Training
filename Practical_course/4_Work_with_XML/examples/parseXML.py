import xml.etree.cElementTree as ET

def parseXML(xml_file):
    '''Парсинг XML при помощи ElementTree'''
    tree = ET.ElementTree(file=xml_file)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    for child in root:
        print(child.tag, child.attrib)
        if child.tag == "appointment":
            for step_child in child:
                print(step_child.tag)

    # Парсинг всей XML структуры
    print("-" * 40)
    print("interating using tree iterator")
    print("-" * 40)
    iter_ = tree.getiterator()

    for elem in iter_:
        print(elem.tag)

    # Получение данных используя дочерние элементы
    print("-" * 40)
    print("Обработка дочерних элементы getchildren()")
    print("-" * 40)
    # appointments = root.getchildren()

    # for appointment in appointments:
    #     appt_children = appointment.getchildren()
    #     for appt_child in appt_children:
            # print("%s=%s" % (appt_child.tag, appt_child.text))


if __name__ == "__main__":
    parseXML("appt.xml")
