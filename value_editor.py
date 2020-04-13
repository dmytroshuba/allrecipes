import xml.etree.ElementTree as ET

tree = ET.parse("recipes.xml")
parent = tree.getroot()


# модифікування текстових значень елементів (додавання) (2-3 значення)
def add_prefix_to_title(prefix, amount):
    counter = 0
    for item in parent.findall('Recipe'):
        if counter != amount:
            title = item.find("Title")
            rating = item.find("Rating")
            print("Title: " + title.text.strip())
            print("Rating: " + rating.text.strip())
            title.text = prefix + title.text.strip()
            rating.text = prefix + rating.text.strip()
            print("\n modified:")
            print("Title: " + title.text.strip())
            print("Rating: " + rating.text.strip())
            counter = counter + 1
        else:
            break
    tree.write("recipes.xml")
    print("done")


# модифікування текстових значень елементів (видалення) (2-3 значення)
def remove_prefix_from_title(prefix, amount):
    counter = 0
    for item in parent.findall('Recipe'):
        if counter != amount:
            title = item.find("Title")
            rating = item.find("Rating")
            print("Title: " + title.text.strip())
            print("Rating: " + rating.text.strip())
            text = title.text.strip()
            ratingText = rating.text.strip()
            if text.startswith(prefix):
                title.text = text[len(prefix):]
            if ratingText.startswith(prefix):
                rating.text = ratingText[len(prefix):]
            print("\n modified:")
            print("Title: " + title.text.strip())
            print("Rating: " + rating.text.strip())
            counter = counter + 1
        else:
            break
    tree.write("recipes.xml")
    print("done")


add_prefix_to_title("test", 2)
remove_prefix_from_title("test", 2)


# модифікування атрибутів складних елементів (додавання) (2-3 значення)
def add_attr(attr, amount):
    counter = 0
    for item in parent.findall('Recipe'):
        if counter != amount:
            item.attrib[attr] = "123"
            item.attrib[attr + "1"] = "1234"
            counter = counter + 1
        else:
            break
    tree.write("recipes.xml")
    print("done")


# модифікування атрибутів складних елементів (видалення) (2-3 значення)
def remove_attr(attr, amount):
    counter = 0
    for item in parent.findall('Recipe'):
        if counter != amount:
            try:
                del item.attrib[attr]
            except KeyError:
                pass
            try:
                del item.attrib[attr + "1"]
            except KeyError:
                pass
        else:
            break
    tree.write("recipes.xml")
    print("done")


add_attr("test", 2)
# remove_attr("test", 2)
