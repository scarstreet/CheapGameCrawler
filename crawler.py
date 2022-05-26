import requests, re
import time
from db import webs
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd

class Format:
    def __init__(self, format):
        self.not_found = re.compile(format['RE_notFound'])
        self.element = re.compile(format['RE_element'])
        self.price = re.compile(format['RE_price'])
        self.image = re.compile(format['RE_image'])
        self.title = re.compile(format['RE_title'])
        
        self.currency = format['currency']
        self.toNTD = format['toNTD']

    def findInfos(self,html):
        data = []
        if(len(self.not_found.findall(html)) != 1):
            elements = self.element.findall(html)
            if(len(elements) > 10):
                elements = elements[:10]
            for el in elements:
                info = {}
                info['price'] = self.price.findall(el)
                if(len(info['price']) == 0):
                    info['price'] = '0'
                else:
                    info['price'] = info['price'][0]
                    if(info['price'] == 'Free' or info['price'] == 'FREE' or info['price'] == 'Free To Play'):
                        info['price'] = '0' 
                    info['price'] = self.numbersOnly.findall(info['price'])[0]
                    if(self.currency != 'NTD'):
                        info['price'] = f"{(float(info['price'].replace(',',''))*self.toNTD):.2f}"
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
    
    currency = ''
    toNTD = ''
    numbersOnly = re.compile('[\d\.,]+')

def toSearchURL(toSearch,web):
    searchInput = web['format']['urlSpace'].join(toSearch.split(' '))
    url = web['format']['requestURL'].split(' ')
    if(len(url)==2):
        url = ''.join([url[0],searchInput,url[1]])
    else:
        url = web['format']['requestURL']+searchInput
    return url

def getHTML(url, browser):
    browser.get(url)
    html = browser.page_source.replace('\n','')
    return html

def search(toSearch):
    results = {}
    driverPath = 'chromedriver.exe'
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(driverPath, options=options)

    for web in webs:
        url = toSearchURL(toSearch,web)
        html = getHTML(url, browser)
        format = Format(web['format'])
        data = format.findInfos(html)
        results[web['name']]=data
    for result in results:
        if(len(results[result]) > 0):
            results[result] = toDF(results[result])
            results[result] = downloadImages(results[result], result)
    return results

def toDF(dict):
    df = pd.DataFrame(dict)
    df.loc[df["price"] == "", "price"] = '0'
    data = []
    for d in df['price']:
        data.append(d.replace(',', ''))
    df['price'] = pd.Series(data)
    df['price'] = df['price'].astype('float')
    df = df.set_index('price')
    df = df.sort_index()
    return df

def downloadImages(df, name):
    data = []
    for id,d in enumerate(df['image'].values.tolist()):
        img_data = requests.get(d).content
        with open(f'images\\{name}-{id}.png', 'wb') as handler:
            handler.write(img_data)
        data.append(f'images\\{name}-{id}.png')
    df['imgPath'] = data
    return df