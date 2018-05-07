from __future__ import division
import time
import os
import sys
import requests
import json
from flask import Flask,request,jsonify
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import operator
import nltk
import string
import indicoio
from newsapi import NewsApiClient
import pickle
indicoio.config.api_key = '156f964fda0804875b7d12fd1d3170bc'

app=Flask(__name__)

@app.route('/api/<query>', methods=['GET','POST'])
def fknscore(query):
    resp=indicoio.keywords(query)
    resp=sorted(resp, key=lambda x:x[1],reverse=True)
    #TOI
    print resp
    search=""
    for a in resp[0:4]:
        search=search+str(a)+" "
    print search
    # baseUri = "https://timesofindia.indiatimes.com/topic/"
    # url = baseUri+search+"/news"
    # try:
    #   result = requests.get(url, verify=True)
    #   result.raise_for_status()
    #
    # except HTTPError:
    #   print "could not download page"
    #
    # soup = BeautifulSoup(result.content, 'html.parser')
    # titles = soup.find_all('span',class_='title')
    newsapi = NewsApiClient(api_key='dc5b60b969b04d18abf625969e604d69')
    all_articles = newsapi.get_everything(q=search,
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    print all_articles

    headings = []
    for article in all_articles['articles']:
        headings.append(article['title'])
    # for title in titles:
    #     headings.append(title.contents[0].encode("utf-8")[1:-1])
    # print headings
    relevances={}
    for heads in headings[0:4]:
        print query
        print heads
        ans=indicoio.relevance(query, [heads])
        print ans
        relevances.update({heads:float(ans[0])})
    #resp=json.dumps(ans)
    score=max(relevances.values())
    #sentimentcheck
    for a,b in zip(relevances.keys(),relevances.values()):
        if b==score:
            relhead=a
    sentiment=indicoio.sentiment([relhead,query])
    print sentiment
    sentivar=abs(float(sentiment[1])-float(sentiment[0]))
    print relhead
    print sentivar
    classifier=pickle.load(open('pacmodel.pkl', 'rb'))
    vectorizer=pickle.load(open('vectorizer.pkl', 'rb'))
    vectors=vectorizer.transform([relhead])
    prediction=classifier.predict(vectors)
    print prediction
    return jsonify({
        'query': query,
        'score':(0.3-float(prediction[0])*0.3)+(score*.49)+.21*(1-sentivar)
    })

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True)
