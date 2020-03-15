import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree
from lxml import etree

url = "https://www.allrecipes.com/"
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 ' \
        'Safari/605.1.15 '

xml = etree.Element('Recipes')
xml_file = ElementTree.ElementTree()
xml_file._setroot(xml)


def get_recipes(response_text):
    recipes = BeautifulSoup(response_text, 'html.parser').findAll("article", {"class": "fixed-recipe-card"})
    for recipe in recipes[:10]:
        process_recipe_details(recipe)

    xml_file.write("recipes.xml")


def process_recipe_details(recipe):
    details = recipe.find("div", {'class': 'fixed-recipe-card__info'})

    href = details.find('h3', {'class': 'fixed-recipe-card__h3'}).find('a', href=True)['href']
    title = details.find('span', {'class': 'fixed-recipe-card__title-link'}).text
    rating = details.find('div', {'class': 'fixed-recipe-card__ratings'}).find('span')['aria-label']
    desc = details.find('div', {'class': 'fixed-recipe-card__description'}).text
    author_link = details.find('div', {'class': 'fixed-recipe-card__profile'}).find('a', href=True)['href']
    author = details.find('ul', {'class': 'cook-submitter-info'}).find('h4').text

    print_recipe(title, href, rating, author, desc, author_link)

    from XMLGenerator import create_xml_from_recipe
    xml_object = create_xml_from_recipe(title, href, rating, author, desc, author_link)
    xml.append(xml_object)


def print_recipe(recipe_title, recipe_link, stars, recipe_author, desc, author_url):
    print(
        " Recipe: ", recipe_title, '\n',
        "Link: ", recipe_link, '\n',
        "Rating: ", stars, '\n',
        "Description: ", desc, '\n',
        "Author: ", recipe_author, '\n',
        "Author link: ", author_url, '\n',
        '\n -------------------------------------')


get_recipes(requests.get(url, headers={'User-Agent': agent}).text)
