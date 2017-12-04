from bs4 import BeautifulSoup
import sys
import requests
import time
import json
from requests.exceptions import HTTPError


searchQuery = sys.argv[1]
searchQuery = searchQuery.replace(" ", "+")
baseUri = "http://indianexpress.com/?s="

url = baseUri+searchQuery

try:
  result = requests.get(url, verify=True)
  result.raise_for_status()

except HTTPError:
  print "could not download page"

else:
  soup = BeautifulSoup(result.content, 'html.parser')
  aTags = soup.select('div.content > a')
  aTags = soup.select('div.search-result > div.details > div.picture > a')
  links = []

  for aTag in aTags:
    links.append(aTag['href'])

  outFile = open("dumps/articlesIE.json","w")
  articles = []

  for link in links:
    article = {}
    try:
      articlePage = requests.get(link, verify=True)
      articlePage.raise_for_status()

    except HTTPError:
      print "unable to download article"

    else:
      soup = BeautifulSoup(articlePage.content, 'html.parser')
      if(soup.select_one('div.heading-part > h1').text and soup.select('div[class="full-details"] > p')):
        article['title'] = soup.select_one('div.heading-part > h1').text
        
        paragraphs = soup.select('div[class="full-details"] > p')
        paragraphs = paragraphs[:-1]

        content = ""
        for paragraph in paragraphs:
           content += paragraph.text

        article['content'] = content

        articles.append(article)
        print article
      
      else:
      	continue

print articles
json.dump(articles,outFile)
outFile.close()