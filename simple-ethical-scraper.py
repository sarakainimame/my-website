# HackerNews web scraper
## 2 page scaper to gather the latest news with more than 100 upvotes 

# Libs we need:
## pip install beautifulsoup4
## pip install requests

#######################################################################
import requests
from bs4 import BeautifulSoup
import pprint as pp # that's pretty print

# requests variable
res = requests.get("https://news.ycombinator.com/")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
# creating a soups
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

#######################################################################
# seach for CSS selectors
# print(soup.body) find(a), find(div)
# print (soup.find(id="score_20514755"))
#######################################################################

# grabbing the links
links = soup.select(".storylink")
links2 = soup2.select(".storylink")

# grabbing the votes
subtext = soup.select(".subtext")
subtext2 = soup2.select(".subtext")

all_links = links + links2
all_subtext = subtext + subtext2

# sorting with a lambda function via key : votes
def sort_story(newslist):
	return sorted(newslist, key= lambda k:k["votes"], reverse=True)

# grabbing titles, votes, links from the subtext in the site
def create_custom_news(links, subtext):
	news = []
	for index, item in enumerate(links): #
		title = links[index].getText()
		href = links[index].get("href", None)
		vote = subtext[index].select(".score")
		if len(vote): 
			points = int(vote[0].getText().replace(" points", ""))
			if points > 99:
				news.append({"title": title, "link": href, "votes": points})

	return sort_story(news)

pp.pprint(create_custom_news(all_links, all_subtext))