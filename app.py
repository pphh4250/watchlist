from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

@app.route('/user/<yourname>')
def user_page(yourname):
    return 'User: %s' %yourname

