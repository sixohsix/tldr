
import urllib2
from elementtree.ElementTree import parse

def getDeliciousRssAsElt(deliciousUser, count=30):
    return parse(urllib2.urlopen(
        "http://feeds.delicious.com/v2/rss/%s?count=%i" %(
            deliciousUser, count)))

def getRecentLinks(deliciousElt, age=None):
    


                           