import requests, re
from bs4 import BeautifulSoup as bs

class Format:
    def __init__(self, req, redir, price, image, title):
        pass
    request_url = ''
    redirect_url = ''
    price = ''
    image = ''
    title = ''

class Web:
    def __init__(self, name, url, format):
        for form in format:
            # TODO - make the format classes here from a dictionary
            pass
        pass
    store_name = ''

