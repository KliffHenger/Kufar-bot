import requests
import re
from bs4 import BeautifulSoup as bs




def urlify(s):
    s = s.strip().split(" ")
    x = ("%20").join(s)
    return x

def get_item(region, keyword):
    urla = f'https://www.kufar.by/{region}?cmp=0&ot=1&query={keyword}&sort=lst.d'
    r = requests.get(urla)
    soup = bs(r.text, "html.parser")
    pattern = r"rank=0"
    try:
        all_find = soup.findAll('section')
        for data in all_find:
            url_itm = data.a['href']
            if re.search(pattern, url_itm):
                x = url_itm[:-46]
                yyy = data.find('a').select('span')
                yy = str(yyy[0])
                y = yy[6:-7]
                img = data.img['src']
                return x, y, img
    except:
        print(f'Парсер не понял - {urla}')        


        # find_href = soup.find('section')# .select('a', class_='styles_wrapper__IMYdY')
        # # print(find_href)
        # # find_price = soup.find('p', class_='styles_price__tiO8k').select('span')
        # find_price = soup.find('section').select('span')
        # find_img = soup.find('section')
        # xx = find_href.a['href'] # https://www.kufar.by/item/201137193?searchId=0925bf5518aa56ccd9871e69b1d739940c5a
        # # print(xx)
        # if re.fullmatch(pattern, xx):  
        #     x = xx[:-46]
        #     y = find_price[0].text
        #     img = find_img.img['src']
        #     return x, y, img
    

# https://www.kufar.by/l/r~shchuchin?cmp=0&ot=1&query=часы&sort=lst.d
# print(get_item('l/r~shchuchin', 'часы'))


# urla = f'https://jetlend.ru/borrower/'
# r = requests.get(urla)
# soup = bs(r.text, "html.parser")
# find_all = soup.find_all()
# print(len(find_all))


