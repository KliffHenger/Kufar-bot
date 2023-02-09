import requests
from bs4 import BeautifulSoup as bs





# https://www.kufar.by/l/r~gomel
# https://www.kufar.by/l/r~gomel?ot=1&query=%D1%81%D1%82%D0%B8%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%B0&utm_queryOrigin=Manually_typed
# URL_TEMPLATE = "https://www.kufar.by/l/r~gomel?cmp=0&sort=lst.d"
# URL_TEMPLATE = f'https://www.kufar.by/l/r~gomel?cmp=0&ot=1&query={keyword}&sort=lst.d'

def urlify(s):
    s = s.strip().split(" ")
    x = ("%20").join(s)
    return x



def get_url(keyword):
    try:
        URL_TEMPLATE = f'https://www.kufar.by/l/r~gomel?cmp=0&ot=1&query={keyword}&sort=lst.d'
        # print(URL_TEMPLATE)
        r = requests.get(URL_TEMPLATE)
        soup = bs(r.text, "html.parser")
        # find_href = soup.find_all('section')
        find_href = soup.find('section')# .select('a', class_='styles_wrapper__IMYdY')
        x = find_href.a['href']
        # for item in find_href:
        #     x = item.a['href']
        #     break
        # print(x)
        return x
    except:
        pass


get_url('hp')
    

def get_price(keyword):
    URL_TEMPLATE = f'https://www.kufar.by/l/r~gomel?cmp=0&ot=1&query={keyword}&sort=lst.d'
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    find_price = soup.find('p', class_='styles_price__tiO8k').select('span')
    y = find_price[0].text
    # print(y)
    return y

