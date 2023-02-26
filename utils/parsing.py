import requests
from bs4 import BeautifulSoup as bs




def urlify(s):
    s = s.strip().split(" ")
    x = ("%20").join(s)
    return x

def get_item(region, keyword):
    urla = f'https://www.kufar.by/{region}?cmp=0&ot=1&query={keyword}&sort=lst.d'
    r = requests.get(urla)
    soup = bs(r.text, "html.parser")
    find_href = soup.find('section')# .select('a', class_='styles_wrapper__IMYdY')
    # find_price = soup.find('p', class_='styles_price__tiO8k').select('span')
    find_price = soup.find('section').select('span')
    x = find_href.a['href']
    y = find_price[0].text
    return x, y

# print(get_item('l/r~shchuchin', 'шуруповерт'))

