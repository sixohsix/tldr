
import sys
import os
from BeautifulSoup import BeautifulSoup
from elementtree.ElementTree import fromstring
from urllib2 import urlopen

from rss import *
from debone import *

tmp_dir = "/tmp"

def main():
    if (sys.argv[1:]):
        links = [("Link", url) for url in sys.argv[1:]]
    else:
        links = getRecentLinks('sixohsix')

    for title, url in links:
        print "====", title.encode('utf-8')
        print "====", url
        try:
            docHtml = urlopen(url)
            doc = BeautifulSoup(docHtml)
            doc = deboned(doc)
            tmp_fn = tmp_dir + os.sep + "tldr.tmp.html"
            open(tmp_fn, "w").write(str(doc))
            url = "file://" + tmp_fn
        except Exception, e:
            print("Warning: Could not debone document.")
            import traceback
            traceback.print_exception(*sys.exc_info())
        print getUrlAsText(url).strip().encode('utf-8')
        print
