import requests
from bs4 import BeautifulSoup as bs
from airtable_config import table






def urlify(s):
    s = s.strip().split(" ")
    x = ("%20").join(s)
    return x



def get_url(keyword):
    try:
        URL_TEMPLATE = f'https://www.kufar.by/l/r~gomel?cmp=0&ot=1&query={keyword}&sort=lst.d'
        r = requests.get(URL_TEMPLATE)
        soup = bs(r.text, "html.parser")
        find_href = soup.find('section')# .select('a', class_='styles_wrapper__IMYdY')
        x = find_href.a['href']
        return x
    except:
        pass


get_url('hp')
    

def get_price(keyword):
    URL_TEMPLATE = f'https://www.kufar.by/l/r~gomel?cmp=0&ot=1&query={keyword}&sort=lst.d'
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    try:
        find_price = soup.find('p', class_='styles_price__tiO8k').select('span')
        y = find_price[0].text
        return y
    except:
        pass
    

    

