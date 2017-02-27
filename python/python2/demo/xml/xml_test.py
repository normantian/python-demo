# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
#l.etree.ElementTree as ET

tree = ET.parse('D:/dev/Python/demo/xml/test2.xml')
para = tree.findall('para')
print len(para)

countries = tree.findall('country')
for c in countries:
    c.getchildren()

for c in countries:
    for child in c.getchildren():
        print child.tag,child.text,child.attrib
    print '='*10
