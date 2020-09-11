import time
from flask import Flask
import YelpApi

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/justPick')
def get_just_pick():
    return {'justPick': YelpApi.business_search_results()}


if __name__ == '__main__':
    app.run(debug=True)