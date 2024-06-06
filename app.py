from flask import Flask, jsonify, send_from_directory
import requests
from textblob import TextBlob
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_static_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/quote', methods=['GET'])
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    quote_data = response.json()
    quote = quote_data['content']
    sentiment = analyze_sentiment(quote)
    return jsonify({'quote': quote, 'sentiment': sentiment})

def analyze_sentiment(quote):
    analysis = TextBlob(quote)
    return analysis.sentiment.polarity

if __name__ == '__main__':
    app.run(debug=True)

