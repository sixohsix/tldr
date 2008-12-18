
def deboned(doc):
    body = doc.find("body")
    
    # Remove all divs that have "nav" in class or id.
    divs = body.findAll("div")
    for div in divs:
        if div.get("id", "").count("nav") or div.get("class", "").count("nav"):
            div.clear()
    return doc
