from flask import Flask, request, jsonify, redirect, render_template
import random
import string
import os

app = Flask(__name__)


url_mapping = {}

def generate_short_url(length=6):
    """Generate a random short URL."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data['url']
    
   
    short_url = generate_short_url()
    while short_url in url_mapping:
        short_url = generate_short_url()
    
   
    url_mapping[short_url] = original_url
    
   
    return jsonify({'shortened_url': f'http://localhost:5000/{short_url}'})

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)