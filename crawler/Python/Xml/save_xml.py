from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

data = [
    ["Iron Man","2008","tt0371746","movie"],
    ["Iron Man 3","2013","tt1300854","movie"],
    ["Iron Man 2","2010","tt1228705","movie"],
    ["The Man in the Iron Mask","1998","tt0120744","movie"],
    ["The Man with the Iron Fists","2012","tt1258972","movie"],
    ["Tetsuo, the Iron Man","1989","tt0096251","movie"],
    ["The Man with the Iron Heart","2017","tt3296908","movie"],
    ["The Invincible Iron Man","2007","tt0903135","movie"],
    ["Iron Man: Rise of Technovore","2013","tt2654124","movie"],
    ["The Man with the Iron Fists 2","2015","tt3625152","movie",]
]

root = Element('root', {'totalResults': '81', 'response': 'True'})
for d in data:
    SubElement(root, 'result',
        {'title': d[0], 'year': d[1], 'imdbID': d[2], 'type': d[3]}
    )

raw_str = tostring(root, 'utf-8')
parsed = minidom.parseString(raw_str)
print(parsed.toprettyxml(indent="  "))

