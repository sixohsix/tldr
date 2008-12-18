
_BAD_THINGS = ["nav", "advertisement", "header", "footer", "comments", "copyright", "caption"]

def deboned(doc):
    body = doc.find("body")

    # Remove all divs that have "nav" in class or id.
    divs = body.findAll("div")
    for div in divs:
        for thing in _BAD_THINGS:
            if div.get("id", "").count(thing) or div.get("class", "").count(thing):
                div.extract()
    return doc
