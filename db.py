webs = [
    {
        "name":'Epic Games',
        "url":'https://store.epicgames.com/',
        "currency":'NTD',
        "toNTD":1,
        "format":{
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
        "currency":'NTD',
        "toNTD":1,
        "format":{
            "requestURL" : 'https://store.steampowered.com/search/?term=',
            "urlSpace": '+',
            "RE_element":'(<a.*?search_result_row.*?</a>)',
            "RE_price" : '(Free To Play|Free|NT\$ [\d.,]+)[^(</strike>)]*?</div>',
            "RE_image" : '<img src=\"(.*?)\".*?>',
            "RE_title" : '<span class=\"title\">(.*?)</span>',
            "RE_notFound": '0 results match your search',
        }
    },
]




