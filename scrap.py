import requests
from bs4 import BeautifulSoup
import pprint

res= requests.get("https://news.ycombinator.com/")
res2=requests.get("https://news.ycombinator.com/news?p=2")
soup=BeautifulSoup(res.text,'html.parser')
soup2=BeautifulSoup(res2.text,'html.parser')

links1=soup.select('.storylink')
subtext1=soup.select(".subtext")
links2=soup2.select('.storylink')
subtext2=soup2.select(".subtext")


all_links=links1+links2
all_text=subtext1+subtext2

def sort_by_votes(hlist):
	return sorted(hlist,key=lambda k:k['votes'],reverse=True)

def create_custom_news(links,subtext):
	hNews=[]

	for idx,item in enumerate(links):
		title=links[idx].getText()
		href=links[idx].get('href',None)
		vote=subtext[idx].select('.score')
		if len(vote):
			points=int(vote[0].getText().replace(" points",""))
			if points>99:
				hNews.append({'title':title,'links':href,'votes':points})


	return sort_by_votes(hNews)

pprint.pprint(create_custom_news(all_links,all_text))