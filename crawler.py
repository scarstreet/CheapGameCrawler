# db is the database of websites. Each containing:
# - name of the store
# - url of the store's webstire
# - currency of the store & its conversion to NTD
# - regex strings to crawl each data
from db import webs

import requests, re
import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options

global DEBUG
DEBUG = False

'''======================================================
A class to define the regex formats of what will
need to be crawled from each website and a function
to extract the crawled items of the website
======================================================'''
class Format:
    '''======================================================
    Functions
    ======================================================'''
    def __init__(self, format):
        # init related to crawling
        self.not_found = re.compile(format['RE_notFound'])
        self.element = re.compile(format['RE_element'])
        self.price = re.compile(format['RE_price'])
        self.image = re.compile(format['RE_image'])
        self.title = re.compile(format['RE_title'])
        
        # init related to currency
        self.currency = format['currency']
        self.toNTD = format['toNTD']

    def findInfos(self,html):
        data = []
        # making sure there is a search result in the web befor
        # crawling. sometimes some webs don't have some games
        if(len(self.not_found.findall(html)) != 1):
            # finding the data element of the web. Containing
            # the info of each game's price, title and image
            elements = self.element.findall(html)

            # Limiting the search result for each web to 10
            # to not overload the app & not waste time on
            # irrelevant results
            if(len(elements) > 10):
                elements = elements[:10]
            
            # Crawling data from each element
            for el in elements:
                try:
                    info = {}
                    # Price ========================================================
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

                    # Title ========================================================
                    print(self)
                    info['title'] = self.title.findall(el)[0]

                    # Image ========================================================
                    # the src link to the image
                    info['image'] = self.image.findall(el)[0]

                    # appending the information to a list that will be returned later on
                    data.append(info)
                except Exception as e:
                    print(e)
        return data
    '''======================================================
    Class Data
    ======================================================'''
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

'''======================================================
Functions to do the crawling process
======================================================'''
# Main search function
def search(toSearch):
    results = {}
    driverPath = 'chromedriver.exe'
    options = Options()
    browser = webdriver.Chrome(driverPath, options=options)
    if not DEBUG:
        browser.set_window_position(-10000,0)

    for web in webs:
        # crawling from each website in the database
        url = toSearchURL(toSearch,web)
        html = getHTML(url, browser)
        format = Format(web['format'])
        data = format.findInfos(html)
        results[web['name']]=data
        if (DEBUG):
            print(web['name']+'============================================')
            print(results[web['name']],end='\n\n\n')
    for result in results:
        # Turning existing results to data frames and downloading
        # Their pictures
        if(len(results[result]) > 0):
            results[result] = toDF(results[result])
            results[result] = downloadImages(results[result], result)
    return results

# Function to generate the url used to instantly search
def toSearchURL(toSearch,web):
    searchInput = web['format']['urlSpace'].join(toSearch.split(' '))
    url = web['format']['requestURL'].split(' ')
    if(len(url)==2):
        url = ''.join([url[0],searchInput,url[1]])
    else:
        url = web['format']['requestURL']+searchInput
    return url

# getting the searched url's source html
def getHTML(url, browser):
    browser.get(url)
    time.sleep(3)
    html = browser.page_source.replace('\n','')
    return html

# Converting the search result to a dataframe instead of a dictionary
# along with sorting the search result by price
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
    df = df.reset_index()
    return df

# downloading the images based on the dataframe
# and adding the image's path for each data to the
# data frame
def downloadImages(df, name):
    data = []
    for id,d in enumerate(df['image'].values.tolist()):
        img_data = requests.get(d).content
        namee = name.replace('.', '')
        end = ".png"
        if("GOG" in namee):
            # an error occured when using GOG it's not solved yet
            # and idk what's causing it. But since it's not important
            # for the topic, I shall let it be 
            end = ".jpg"
        with open(f'images\\{namee}-{id}{end}', 'wb') as handler:
            handler.write(img_data)
        data.append(f'images/{namee}-{id}{end}')
    df['imgPath'] = data
    return df

DEBUG = True
# search('phasmo')