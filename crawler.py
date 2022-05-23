import requests, re
from db import webs
from bs4 import BeautifulSoup as bs
from selenium import webdriver

class Format:
    def __init__(self, format):
        self.redirect_url = re.compile(format['RE_redirectURL'])
        # self.priceFormat = re.compile(format['RE_priceFormat'])
        self.not_found = re.compile(format['RE_notFound'])
        self.element = re.compile(format['RE_element'])
        self.price = re.compile(format['RE_price'])
        self.image = re.compile(format['RE_image'])
        self.title = re.compile(format['RE_title'])

    def findInfos(self,html):
        data = []
        if(len(self.not_found.findall(html)) == 0):
            elements = self.element.findall(html)
            print(len(elements))
            for el in elements:
                info = {}
                info['price'] = self.price.findall(el)[0]
                info['title'] = self.title.findall(el)[0]
                info['image'] = self.image.findall(el)[0]
                data.append(info)
        return data
    redirect_url = ''
    priceFormat = ''
    not_found = ''
    element = ''
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

def toSearchURL(toSearch,web):
    searchInput = web['format']['urlSpace'].join(toSearch.split(' '))
    url = web['format']['requestURL'].split(' ')
    url = ''.join([url[0],searchInput,url[1]])
    return url

def getHTML(url, browser):
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html

def search(toSearch):
    results = []
    driverPath = 'chromedriver.exe'
    browser = webdriver.Chrome(driverPath)
    # browser.set_window_position(-10000,0)

    for web in webs:
        url = toSearchURL(toSearch,web)
        html = getHTML(url, browser)

        format = Format(web['format'])
        data = format.findInfos(html)
        print(data)
        pass

search('overcooked')