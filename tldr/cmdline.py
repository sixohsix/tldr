
import sys
import os
from elementtree.ElementTree import parse
from urllib2 import urlopen

from rss import *
from debone import *

tmp_dir = "/tmp"

def main():
    if (sys.argv[1:]):
        links = [("Link", url) for url in sys.argv[1:]]
    else:
        links = getRecentLinks(getDeliciousRssAsElt('sixohsix'))

    for link in links:
        print "====", link[0].encode('utf-8')
        print "====", link[1]
        url = link[1]
        try:
            docHtml = urlopen(link[1])
            doc = parse(docTxt)
            doc = deboned(doc)
            tmp_fn = tmp_dir + os.sep + "tldr.tmp.html"
            doc.write(open(tmp_fn, "w"))
            url = "file://" + tmp_fn
        except:
            pass
        print getUrlAsText(url).strip().encode('utf-8')
        print
