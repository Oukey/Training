# Создание XML-документа:
# 1. Создать корневой элемент
# 2. Создать его дочерние элементы
# 3. Настроить атрибуты и иные характеристики этих элементов

import xml.etree.ElementTree as ETree

# Создание корневого узла
data = ETree.Element('data')

# СОздание дочерних узлов
itm_name = ETree.SubElement(data, 'name')
itm_sex = ETree.SubElement(data, 'sex')
itm_age = ETree.SubElement(data, 'age')
itm_langs = ETree.SubElement(data, 'languages')
itm_pc = ETree.SubElement(data, 'pc')

# Присвоение значений новы узлам
itm_name.text = 'Petya'
itm_sex.text = 'true'
itm_age.text = '23'

itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '9'
itm_l1.set('name', 'Python')
itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '7'
itm_l1.set('name', 'Java')
itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '7'
itm_l1.set('name', 'PHP')

itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = 'Linux'
itm_pc1.set('name', 'os')
itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = 'ram'
itm_pc1.set('name', '64')

# Сериализация XML-документа
# serialze = ETree.tostring(data, encoding='utf8', method='xml').decode()
# fil = open("items.xml", 'w')
# fil.write(serialze)

# Поиск информации в XML-документа
print('!' * 10)
for lng in itm_langs.findall('language'):
    print(lng.text)

print('!' * 10)
item = data.find('pc')
for subitem in item.findall('pc_item'):
    print(subitem.text)

print('!' * 10)
# Перебор всех узлов итератором iter()
for item in data.iter():
    print(item.tag, item.text, item.attrib)

# Модификация узлов
itm_sex.text = "man"
itm_sex.set("sex2", 'false')

# Удаление атрибута
itm_sex.attrib.pop("sex2")

print('!' * 10)
# Удаление всех дочурних узлов
itm_langs.clear()

for item in data.iter():
    print(item.tag, item.text, item.attrib)
