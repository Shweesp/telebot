import requests as rq
import purl
from bs4 import BeautifulSoup

URL = "https://yandex.ru/news"
HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'accept':'*/*'
}

def get_html(url, params=None):
    try:
        r = rq.get(url, params=params, headers=HEADERS)
        
    except Exception as error:
        print("Ошибка:", error)
        return None
        
    return r
    

def get_last_link(text):
    soup = BeautifulSoup(text, 'html.parser')
    item = soup.find('a', class_='mg-card__link')
    link = item.get('href')
    return link 
def parse():
    html = get_html(URL)

    if html.status_code == 200:
        last_link = get_last_link(html.text)
        last_link_id = purl.URL(last_link).query_param("persistent_id")
    else:
        print("Запрос не прошел.\nCode:", html.status_code)
        
    try:
        f = open('file.txt', 'r')
        f_link_id = purl.URL(f.read()).query_param("persistent_id")
        if f_link_id == last_link_id:
            return "Have no news =("
            
        else:
            f.close()
            f = open('file.txt', 'w')
            f.write(last_link)
            return last_link

    except FileNotFoundError:
        f = open('file.txt', 'w')
        f.write(last_link)
        return last_link
        
    finally:
        f.close()



print(parse())
