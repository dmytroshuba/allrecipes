import lxml.etree as ET
import webbrowser

xml_file = "recipes.xml"
xsl_file = "recipes.xsl"
output_file = "output.html"


def create_html(xml, xsl):
    dom = ET.parse(xml)
    xslt = ET.parse(xsl)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    html = ET.tostring(newdom)
    print("Created html: " + str (html))
    return html


def save_output_to_file(text, file):
    f = open(file, 'w+')
    output = str(text)
    f.write(output)
    f.close()


text = create_html(xml_file, xsl_file)
save_output_to_file(text, output_file)
webbrowser.open(output_file, new=2)
