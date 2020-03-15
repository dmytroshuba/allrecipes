from lxml import etree
from termcolor import colored


def get_schema():
    schema_file = 'recipes.xsd'
    with open(schema_file, 'rb') as f:
        schema_root = etree.XML(f.read())

    return etree.XMLSchema(schema_root)


def validate(parser, xml):
    try:
        with open(xml, 'rb') as f:
            etree.fromstring(f.read(), parser)
        return True
    except etree.XMLSchemaError:
        print(colored('XMLSchemaError', 'red'))
        return False
    except etree.XMLSyntaxError:
        print(colored('XMLSyntaxError', 'red'))
        return False


parser = etree.XMLParser(schema=get_schema())

xml = 'recipes.xml'
if validate(parser, xml):
    print(colored("%s validation status - OK" % xml, 'blue'))
else:
    print(colored("%s validation status - ERROR" % xml, 'red'))
