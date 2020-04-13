import xml.etree.ElementTree as ET

# модифікування атрибутів складних елементів (додавання/видалення) (2-3 значення)
tree = ET.parse("recipes.xml")
parent = tree.getroot()


def add_attr(attr, amount):
    counter = 0
    for item in parent.findall('Recipe'):
        if counter != amount:
            item.attrib[attr] = "123"
            counter = counter + 1
        else:
            break
    tree.write("recipes.xml")
    print("done")


def remove_attr(attr, amount):
    counter = 0
    for item in parent.findall('Recipe'):
        if counter != amount:
            try:
                del item.attrib[attr]
            except KeyError:
                pass
        else:
            break
    tree.write("recipes.xml")
    print("done")


add_attr("test", 2)
remove_attr("test", 2)
