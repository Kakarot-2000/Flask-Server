# create requirements file
# deploy server to online hosting service

import json
from flask import Flask, request, jsonify, Response
import nlpcloud
from flask_cors import CORS, cross_origin
import trafilatura
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app, support_credentials=True)

load_dotenv()
# Get the API token from the .env file.
TOKEN = os.getenv("token")


client = nlpcloud.Client(
    "bart-large-cnn", TOKEN)


@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getSummary():
    print('body is ')
    req = request.get_json()
    print(req['url'])
    downloaded = trafilatura.fetch_url(req['url'])
    text = trafilatura.extract(downloaded)
    print(text[:1000])
    response = client.summarization(text[:1000])
    print(response['summary_text'])
    resp = Response(response['summary_text'])
    print(type(resp))
    return resp


app.run(debug=True)
