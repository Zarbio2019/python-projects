# Author: Zarbio Romulo

from flask import Flask, jsonify

'''
# Sample
# When run in Replit.com it show this url for the API like public: https://create-your-own-currency-rate-api.ardits.repl.co
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

app.run(host='0.0.0.0')
'''

# get the rate from web
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate

app = Flask(__name__)

# build API response in json
@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  rate = get_currency(in_cur, out_cur)
  result_dictionary = {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
  return jsonify(result_dictionary) # convert from object to json

app.run(host='0.0.0.0') # localhost
