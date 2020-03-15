from lxml import etree


def create_xml_from_recipe(recipe_title, recipe_link, stars, recipe_author, desc, author_url):
    root = etree.Element('Recipe')

    title = etree.Element('Title')
    link = etree.Element('Link')
    rating = etree.Element('Rating')
    description = etree.Element('Description')
    author = etree.Element('Author')
    author_link = etree.Element('AuthorLink')

    title.text = recipe_title
    link.text = recipe_link
    rating.text = stars
    description.text = desc
    author.text = recipe_author
    author_link.text = author_url

    root.append(title)
    root.append(link)
    root.append(rating)
    root.append(description)
    root.append(author)
    root.append(author_link)
    return root
