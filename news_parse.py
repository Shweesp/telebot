'''
Parsing for Russian news. Yandex.News
By VlaDick for telebot "@deddoublepythonbot"
© Double python corp. 2021. All rights reserved.
'''

# Main libs imports
import requests as rq
import purl
from bs4 import BeautifulSoup

# Config imports
from config import URL, HEADERS


# HTML page getter
def get_html(url, params=None):
    try:
        r = rq.get(url, params=params, headers=HEADERS)

    except Exception as error:
        print("Ошибка:", error)
        return False

    return r


# Parse link of latest new in the news list
def get_last_link(text):
    soup = BeautifulSoup(text, 'html.parser')
    item = soup.find('a', class_='mg-card__link')
    link = item.get('href')
    return link


# Main func which returns link on the new if it is new. LOL
def parse():
    html = get_html(URL)
    if not html:
        print("Request error.") # Use HTML getter

    # Is it SUCKcessful?
    if html.status_code == 200:
        last_link = get_last_link(html.text) # Link for latest record in list of news
        last_link_id = purl.URL(last_link).query_param("persistent_id") # ID of the latest record

    # If it's not
    else:
        print("Incorrect answer from server.\nAnswer code:", html.status_code)

    # Work with file
    try:
        f = open('file.txt', 'r')
        f_link_id = purl.URL(f.read()).query_param("persistent_id") # Gets last record's ID from file

        # Is this a new record?
        if f_link_id == last_link_id:
            return False

        # If it is
        else:
            f.close()
            f = open('file.txt', 'w')
            f.write(last_link) # Rewrite latest new in the file
            return last_link

    # For first activate
    except FileNotFoundError:
        f = open('file.txt', 'w')
        f.write(last_link)
        return last_link

    # Exception handler
    except Exception as exp:
        print("Open file error:\n{}".format(exp))

    finally:
        f.close()


if __name__ == "__main__":
    print(parse())
