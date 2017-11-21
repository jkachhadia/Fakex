import time
import os
import sys
import requests
import json
from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/api/<query>', methods=['GET','POST'])
def fknscore(query):

    return jsonify({
        'query': query,
        'keywords': keywords,
        'score':score,
    })



def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
