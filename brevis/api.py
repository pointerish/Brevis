import json
import hashlib
from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.json['url']
    shortened_url = hashlib.shake_256(url.encode()).hexdigest(5)
    with open('urls.json', 'a') as urls:
        json.dump({shortened_url:url}, urls)
    return jsonify({'shortened_url':shortened_url})

@app.route('/<url_id>', methods=['GET'])
def redirect_to_url(url_id):
    with open('urls.json', 'r') as jf:
        urls = json.load(jf)
    original_url = urls[url_id]
    return redirect(original_url)

@app.route('/')
def root():
    html = '''
    <h1>Brevis URL Shortener</h1>
    <p>Brevis accepts a POST request containing a JSON formatted as such:<li>{"url":"Long URL goes here."}</li>
    This POST request will return a json containing the id of the URL and the client should then send a GET request to
    https://brevis-shortener.herokuapp.com/<URLID> which will redirect to the original URL.</p>
    <p> Of course, the Heroku domain is long and beats the purpose of the shortener, but this is just a proof of concept and a learning 
    project.</p> 
    '''
    return html