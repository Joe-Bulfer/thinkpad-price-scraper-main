from bs4 import BeautifulSoup
import random, requests, json 

    
def get_price_avg(model,search):

    ua_list = ['Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
        ,'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36']

    HEADERS = {
        'user-agent' : random.choice(ua_list),  
        'Accept-Language': 'en-US, en;q=0.5'
    }

    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search + "&_sacat=0&rt=nc&LH_BIN=1"  
    page = requests.get(url, headers = HEADERS) 

    if page.status_code != 200:
        print('Fail to retrieve page.')   
    else:
        print('Retrieved page succesfully.')

    soup = BeautifulSoup(page.content, "lxml")  

    items = soup.find_all(class_ = "s-item__price")

    price_arr = []
    for item in items:
        str_price = item.text
        replaced = str_price.replace("$", "").replace(",", "")
        try:
            if ' to ' not in replaced:  # ignore price ranges
                flt_price = float(replaced)
                price_arr.append(flt_price)
        except ValueError: 
            print(f"Could not convert '{replaced}' to a number.")

    price_arr.pop(0)

    price_avg = sum(price_arr)/len(price_arr)
    retval = {"model": model,"price_avg": price_avg}
    return retval

