from flask import render_template
from app import app

@app.route('/index')   # this does not work
def index():
    #return "Index"
    user = {'username': 'Peter'}
    return render_template('index.html', title='Home', user=user)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name