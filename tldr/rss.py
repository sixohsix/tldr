
import urllib2
import commands
from elementtree.ElementTree import parse

w3mCmd = "/opt/local/bin/w3m"

def getDeliciousRssAsElt(deliciousUser, count=30):
    return parse(urllib2.urlopen(
        "http://feeds.delicious.com/v2/rss/%s?count=%i" %(
            deliciousUser, count)))

def getRecentLinks(rssElt, age=None):
    links = []
    for elt in rssElt.findall("channel/item"):
        if (elt.find('category').text.count("tl;dr")):
            links.append((elt.find('title').text, elt.find('link').text))
    
    return links

def getUrlAsText(url):
    return unicode(commands.getoutput(w3mCmd + " -dump '" + url + "'"), 'utf-8')
    