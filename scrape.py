from bs4 import BeautifulSoup
import random, requests, re, json #Random is used for the following user-agent list, requests is used to request the URL 

ua_list = ['Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    ,'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36']

HEADERS = {
    'user-agent' : random.choice(ua_list),  # The UA is included in the header of an HTTP request sent to the web server
    'Accept-Language': 'en-US, en;q=0.5'
}

def get_ebay_soup(search):
    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search + "&_sacat=0&rt=nc&LH_BIN=1"  
    page = requests.get(url, headers = HEADERS) 

    if page.status_code != 200:
        print('\nFail to retrieve page.\n')   
    else:
        print('\nRetrieved page succesfully.\n')

    soup = BeautifulSoup(page.content, "lxml")  
    return soup

def get_price(soup):
    pattern = re.compile(r'(?i)T480(?!S)', re.IGNORECASE)

    items = soup.find_all(class_ = "s-item")
        
    thinkpad_data = []
    for item in items:
        match = pattern.search(item)
        if match:
            print("junk")
        else:
            replaced = item.replace("$", "")
            flt_price = float(replaced)
            thinkpad_data.append(flt_price)
    thinkpad_data.pop(0)

soup = get_ebay_soup("T430")
price_arr = get_price(soup,"T430S")

# for i in range(len(thinkpad_data)):
#     price = thinkpad_data[i].replace("$", "")
#     thinkpad_data[i] = float(price)

json_data = json.dumps(price_arr)

with open('py_data.json', 'w') as file:
    file.write(json_data)


