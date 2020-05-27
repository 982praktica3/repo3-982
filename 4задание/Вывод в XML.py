import sqlite3
con = sqlite3.connect('pr.db')

import xml.etree.ElementTree as ET
items = ET.Element("items")
def sql_fetch(con):
    
   
    a=0
    cursor = con.cursor()

    cursor.execute('SELECT * FROM info')

    rows = cursor.fetchall()

    for row in rows:

        a=a+1
        b=str(a)
        n = ET.SubElement(items, "\n")
        row = ET.SubElement(items, "row")
        n = ET.SubElement(row, "\n")
        kd = ET.SubElement(row, "  id")
        n = ET.SubElement(row, "\n")
        name = ET.SubElement(row, "  name")
        n = ET.SubElement(row, "\n")
        date = ET.SubElement(row, "  date")
        n = ET.SubElement(row, "\n")
        mobil = ET.SubElement(row, "  mobil")
        n = ET.SubElement(row, "\n")
        toils = ET.SubElement(row, "  toils")
        n = ET.SubElement(row, "\n")
        address = ET.SubElement(row, "  address")
        n = ET.SubElement(row, "\n")
        n = ET.SubElement(items, "\n")

        cursor.execute("SELECT id FROM info WHERE id=?", b)
        r = ET.SubElement(kd, str(cursor.fetchall()))
        cursor.execute("SELECT name FROM info WHERE id=?", b)
        t = ET.SubElement(name, str(cursor.fetchall()))
        cursor.execute("SELECT date FROM info WHERE id=?", b)
        y = ET.SubElement(date, str(cursor.fetchall()))
        cursor.execute("SELECT mobil FROM info WHERE id=?", b)
        u = ET.SubElement(mobil, str(cursor.fetchall()))
        cursor.execute("SELECT toils FROM info WHERE id=?", b)
        i = ET.SubElement(toils, str(cursor.fetchall()))
        cursor.execute("SELECT address FROM info WHERE id=?", b)
        o = ET.SubElement(address, str(cursor.fetchall()))

    tree = ET.ElementTree(items)
    tree.write("bd.xml", encoding='UTF-8', xml_declaration=True)

sql_fetch(con)