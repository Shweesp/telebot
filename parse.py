import requests as rq
from bs4 import BeautifulSoup

URL = "https://mail.ru"
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
	item = soup.find('div', class_='ssr-main')
	link = item.find('a').get('href')
	return link
		
def parse():
	html = get_html(URL)

	if html.status_code == 200:
		last_link = get_last_link(html.text)
	else:
		print("Запрос не прошел.\nCode:", html.status_code)
		
	try:
		file = open('file.txt', 'r')
		
		if file.read() == last_link:
			return False
			
		else:
			file.close()
			file = open('file.txt', 'w')
			file.write(last_link)
			return last_link

	except FileNotFoundError:
		file = open('file.txt', 'w')
		file.write(last_link)
		return last_link
		
	finally:
		file.close()


if __name__ == "__main__":
	print(parse())
