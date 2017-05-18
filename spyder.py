import requests
from bs4 import BeautifulSoup

def crawly(search):
	url = 'https://www.youtube.com/results?search_query='+ search #put url here
	source_code = requests.get(url)
	plain_text = source_code.text
	web_data = BeautifulSoup(plain_text, "html.parser")
	for a in web_data.findAll('a', {'rel': 'spf-prefetch'}): #can change item name here
		href = 'https://www.youtube.com' + a.get('href')
		print(a.string)
		if href[24:29] != 'watch':
			continue
		insider(href)
		print(href+'\n')

def insider(url):
	source_code = requests.get(url)
	plain_text = source_code.text
	web_data = BeautifulSoup(plain_text, "html.parser")
	div = web_data.find('div', {'class': 'watch-view-count'})
	print(div.string)

search_str = input('Enter the search string: ')

crawly(search_str)
exit()
