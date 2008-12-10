
class Article(object):
    def __init__(self, title, text, srcUrl=None):
        self.srcUrl = srcUrl
        self.title = title
        self.text = text
