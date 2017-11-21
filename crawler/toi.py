from bs4 import BeautifulSoup
import requests
import time
import json
from requests.exceptions import HTTPError

basUri = "https://timesofindia.indiatimes.com/topic/delhi-air-pollution/news";

try:
  result = requests.get(basUri, verify=True)
  result.raise_for_status()

except HTTPError:
  print "could not download page"

else:
  soup = BeautifulSoup(result.content, 'html.parser')
  aTags = soup.select('div.content > a')
  links = [];

  for aTag in aTags:
    links.append(basUri+aTag['href'])

  #print links 

  outFile = open("dumps/articles.json","w")
  articles = []

  for link in links:
    article = {};
    try:
      articlePage = requests.get(link, verify=True)
      articlePage.raise_for_status()

    except HTTPError:
      print "unable to download article"

    else:
      soup = BeautifulSoup(articlePage.content, 'html.parser')
      if(soup.select_one('div.main-content > section > h1').text or soup.select_one('arttextxml').text):
        article['title'] = soup.select_one('div.main-content > section > h1').text
        article['content'] = soup.select_one('arttextxml').text;
        articles.append(article)
        print article
      
      else:
      	continue
      #time.sleep(1)


print articles
json.dump(articles,outFile)
outFile.close()