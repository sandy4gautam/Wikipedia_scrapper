import requests
from bs4 import BeautifulSoup
import random
def myscrapper(url):
	response = requests.get(
		url=url,
	)
	soup = BeautifulSoup(response.content,'html.parser')
	title = soup.find(id='firstHeading')
	print(title.text)
	all_links = soup.find(id='bodyContent').find_all('a')
	new_links = []
	for link in all_links:
		try:
			if link['href'].find('/wiki/') != -1:
				if link['href'].find('https:') ==-1:
					new_links.append(link)
		except KeyError:
			continue

	random.shuffle(new_links)

	linkToScrape = random.choice(new_links)

	myscrapper("https://en.wikipedia.org" + linkToScrape['href'])

myscrapper("https://en.wikipedia.org/wiki/Crypto")