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