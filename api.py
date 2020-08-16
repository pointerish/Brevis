import json
import hashlib
from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from flask import render_template

# from forms import URLForm

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'fa61f46c18568ef572057ce5c47f415c'

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
@app.route('/home')
def root():
    return render_template('home.html')    