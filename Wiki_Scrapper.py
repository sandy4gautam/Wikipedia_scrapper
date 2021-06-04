#imports
import requests
from bs4 import BeautifulSoup
import random

#functiuon to scrap wikipedia page titles randomly
def wikiscrapper(url):
	#requesting a response by passing the url
	response = requests.get(url=url,)
	#parsing the html content
	soup = BeautifulSoup(response.content,'html.parser')
	#getting heading from the webpage
	title = soup.find(id='firstHeading')
	#printing the title
	print(title.text)
	#getting all the links from the current webpage
	all_links = soup.find(id='bodyContent').find_all('a')
	#empty list to save only links that have /wiki/ in them and not https links
	#since we only want wikipedia links
	new_links = []
	#for loop to iterate through links and save only wikipedia links in list new_links
	for link in all_links:
		try:
			if link['href'].find('/wiki/') != -1:
				if link['href'].find('https:') ==-1:
					new_links.append(link)
		except KeyError:
			continue

	#getting a random link from the list
	linkToScrape = random.choice(new_links)

	#opening this new randomly selected link and repeating the process again
	wikiscrapper("https://en.wikipedia.org" + linkToScrape['href'])

#calling the function
wikiscrapper("https://en.wikipedia.org/wiki/Crypto")