webs = [
    {
        "name":'Epic Games',
        "url":'https://store.epicgames.com/',
        "format":{
            "currency":'NTD',
            "toNTD":1,
            "requestURL" : 'https://store.epicgames.com/en-US/browse?q= &sortBy=relevancy&sortDir=DESC&count=40',
            "urlSpace": '%20',
            "RE_element":'(<li class=\"css-lrwy1y\".*?</li>)',
            "RE_price" : '<span class=\"css-z3vg5b\" data-component=\"Text\">(NT\$[\d|,|\.]+|Free)</span>',
            "RE_image" : '<img alt=\".+\" src=\"([^\"]+)\"',
            "RE_title" : '<div data-testid=\"direction-auto\" class=\"css-1h2ruwl\" data-component=\"DirectionAuto\">([^<]+)',
            "RE_notFound": '<span data-component=\"Message\">No results found</span>',
        }
    },
    {
        "name":'Steam',
        "url":'https://store.steampowered.com/',
        "format":{
            "currency":'NTD',
            "toNTD":1,
            "requestURL" : 'https://store.steampowered.com/search/?term=',
            "urlSpace": '+',
            "RE_element":'(<a.*?search_result_row.*?</a>)',
            "RE_price" : '(Free To Play|Free|NT\$ [\d.,]+)[^(</strike>)]*?</div>',
            "RE_image" : '<img src=\"(.*?)\".*?>',
            "RE_title" : '<span class=\"title\">(.*?)</span>',
            "RE_notFound": '0 results match your search',
        }
    },
    {
        "name": 'GOG.com',
        "url": 'https://www.gog.com/en',
        "format": {
            "currency": 'USD',
            "toNTD": 29.6,
            "requestURL": 'https://www.gog.com/en/games?query= &order=desc:score',
            "urlSpace": '%20',
            "RE_element": '(<product.*?product-tile>)',
            "RE_price": 'id=\"productTileFinalPrice\">.*?(FREE|\$[\d.,]+)',
            "RE_image": ' type=\"image/webp\" class=\"ng-star-inserted\"><source srcset=\"https://images\.gog-statics\.com/.*?\.jpg, (.*?\.jpg 2x\") type=\"image/jpeg\" class=\"ng-star-inserted\">',
            "RE_title": '<p class=\"product-tile__title\" title=\"(.*?)\"',
            "RE_notFound": 'We couldn’t find anything matching your criteria',
        }
    },
    {
        "name": 'G2A',
        "url": 'https://www.g2a.com/',
        "format": {
            "currency": 'USD',
            "toNTD": 29.6,
            "requestURL": 'https://www.g2a.com/search?query=',
            "urlSpace": '%20',
            "RE_element": '(<li class=\"indexes__Pro.*?</li>)',
            "RE_price": '<span class=\"indexes__PriceCurrentBase.*?\">([\d\.]+)<',
            "RE_image": '<img .*?src=\"(.*?)\" loading=\"lazy\".*?></div>',
            "RE_title": 'class=\"indexes__Title.*?\"><a href=\".*?\" title=\"(.*?)\"',
            "RE_notFound": 'No matching products found',
        }
    },
]




