from bs4 import BeautifulSoup
import requests
import time
import json
from requests.exceptions import HTTPError

basUri = "https://www.washingtonpost.com/newssearch/"
payload = {'query':'delhi', 'sort':'Relevance', 'datefilter':'All%20Since%202005'} 

try:
  result = requests.get(basUri, params=payload, verify=True)
  result.raise_for_status()

except HTTPError:
  print "could not download page"

else:
  soup = BeautifulSoup(result.content, 'html.parser')
  file = open("fucked.html","w")
  file.write(result.content)
  file.close()

  aTags = soup.select('div.pb-results-container > div > a')
  links = []

  for aTag in aTags:
    print aTag['href']
    links.append(aTag['href'])

  print links 

  # outFile = open("dumps/articles.json","w")
  # articles = []

  # for link in links:
  #   article = {}
  #   try:
  #     articlePage = requests.get(link, verify=True)
  #     articlePage.raise_for_status()

  #   except HTTPError:
  #     print "unable to download article"

  #   else:
  #     soup = BeautifulSoup(articlePage.content, 'html.parser')
  #     content = ""
  #     paragraphs = soup.select('div.post-contents > p')

  #     for paragraph in paragraphs:
  #       print paragraph.text
  #       if (paragraph['className'] == ""):
  #         print "gotcha" + paragraph.text 

       # if(soup.select_one('h1.headline__title').text):
       #   article['title'] = soup.select_one('div.main-content > section > h1').text
       #   article['content'] = soup.select_one('arttextxml').text
       #   articles.append(article)
       #   print article
      
#       else:
#       	continue
#       #time.sleep(1)


# print articles
# json.dump(articles,outFile)
# outFile.close()