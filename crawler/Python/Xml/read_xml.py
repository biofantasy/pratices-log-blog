import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()
print(root.attrib)
total = root.attrib['totalResults']
movies = list()
for tag in root.findall('result'):
    print(tag.attrib)
    movies.append(tag.attrib['title'])

print('共', total, '筆資料, 前 10 筆')
print('\n' .join(movies))
