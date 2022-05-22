webs = [
    {
        "name":'Epic Games',
        "url":'https://store.epicgames.com/',
        "currency":'NTD',
        "toNTD":1,
        "format":{
            "requestURL" : 'https://store.epicgames.com/en-US/browse?q= &sortBy=relevancy&sortDir=DESC&count=40',
            "urlSpace": '%20',
            "RE_redirectURL" : '<a class=\"css-1jx3eyg\".+</a>',
            "RE_element":'<li class=\"css-lrwy1y\".+<\li>',
            "RE_price" : '<span class=\"css-z3vg5b\" data-component=\"Text\">[NT,Free].+<\span>',
            "RE_image" : '<img.+</img>',
            "RE_title" : '<div data-testid=\"direction-auto\" class=\"css-1h2ruwl\" data-component=\"DirectionAuto\">(?!<).+</div>',
            "RE_notFound": '<span data-component=\"Message\">No results found</span>',
        }
    },
]




