import xml.etree.ElementTree as ET
from xml.dom import minidom
def main():
    new = ET.Element('items')
    title = ET.SubElement(new, 'row')
    name = ET.SubElement(title, 'name')
    name.text = 'Русалимов Владислав Олегович'
    date = ET.SubElement(title, 'date')
    date.text = '10.09.2001'
    mobil = ET.SubElement(title, 'mobil')
    mobil.text = '89221403056'
    toils = ET.SubElement(title, 'toils')
    toils.text = 'vk'
    address = ET.SubElement(title, 'address')
    address.text = 'п. Полевой'

    save_xml('db1.xml', new)


def save_xml(filename, xml_code):
    xml_string = ET.tostring(xml_code).decode()

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w') as xml_file:
        xml_file.write(xml_prettyxml)


if __name__ == '__main__':
    main()