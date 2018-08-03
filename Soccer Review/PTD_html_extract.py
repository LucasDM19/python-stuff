 # -*- coding: utf-8 -*-

from html.parser import HTMLParser

#Strings de teste
#pstring = source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""
pstring = """<html></html>"""
	
"""
   Esse link: http://stackoverflow.com/questions/11804148/parsing-html-to-get-text-inside-an-element
   Salvou a minha vida.
"""
class myhtmlparser(HTMLParser):
    def __init__(self):
        self.reset()
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []
    def handle_starttag(self, tag, attrs):
        self.NEWTAGS.append(tag)
        self.NEWATTRS.append(attrs)
    def handle_data(self, data):
        self.HTMLDATA.append(data)
    def clean(self):
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []

parser = myhtmlparser()
parser.feed(pstring)

# Extract data from parser
tags  = parser.NEWTAGS
attrs = parser.NEWATTRS
data  = parser.HTMLDATA

# Clean the parser
parser.clean()

# Print out our data
#print "TAGS:" + str(tags)
#print "ATTR:" + str(attrs)
#print "DATA:" + str(data)
print("DATA:")
for d in data:
	x = d.replace("\n","")
	x = x.replace("\t","")
	x = x.replace("  "," ")
	x = x.replace("\t","")
	#print "TAM:" + str(len(x))
	#if len(x) > 5:
		#print x
		#print "<LINHA>" + "TAM:" + str(len(x))
	if "João Paulo" in x:
		print("AVALIA:" + x)