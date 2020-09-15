import json
from hashlib import shake_256
from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/shorten', methods=['POST', 'GET'])
def shorten():
    if request.method == 'GET':
        return render_template('home.html')
    url = request.json['url']
    shortened_url = shake_256(url.encode()).hexdigest(5)
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
@app.route('/home')
def root():
    return render_template('home.html')
