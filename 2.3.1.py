#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom 

def replaceText(node, newText):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("node does not contain text")
    node.firstChild.replaceWholeText(newText)

xml_doc = xml.dom.minidom.parse("test.xml")
movies = xml_doc.getElementsByTagName("movie")
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print ("Title: %s" % movie.getAttribute("title"))
    type = movie.getElementsByTagName('type')[0]
    print ("Type: %s" % type.firstChild.data)
    format = movie.getElementsByTagName('format')[0]
    print ("Format: %s" % format.firstChild.data);
    replaceText(type, "None")

file_handle = open("out_1.xml","wb")
xml_doc.writexml(file_handle)
file_handle.close()
