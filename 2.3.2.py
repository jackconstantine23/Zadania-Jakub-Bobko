import xml.sax, xml.sax.saxutils

class Renamer(xml.sax.saxutils.XMLGenerator):
    def startElement(self, name, attrs):
        self.currenttext = name;
        xml.sax.saxutils.XMLGenerator.startElement(self, name,attrs)
    def endElement(self, name):
        self.currenttext = "";
        xml.sax.saxutils.XMLGenerator.endElement(self, name)
    def characters(self,content):
        if self.currenttext == "format":
            xml.sax.saxutils.XMLGenerator.characters(self, 'test')
        else:
            xml.sax.saxutils.XMLGenerator.characters(self, content)

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print "*****Movie*****"
            title = attributes["title"]
            print "Title:", title
    def endElement(self, tag):
        if self.CurrentData == "type":
            print "Type:", self.type
        elif self.CurrentData == "format":
            print "Format:", self.format
        elif self.CurrentData == "year":
            print "Year:", self.year
            self.CurrentData = ""
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content

parser = xml.sax.make_parser()
parser.setContentHandler(MovieHandler())
parser.parse("test.xml");

file_handle_2 = open("out_2.xml","w")
file_handle_1 = open("test.xml","r")
xml.sax.parse(file_handle_1,Renamer(file_handle_2))

