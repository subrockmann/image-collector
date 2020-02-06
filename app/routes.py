from flask import render_template 
from flask import request, redirect
from flask_wtf import FlaskForm


from werkzeug.utils import secure_filename
from app import app
from pathlib import Path
import os

uploads_folder = Path('/uploads')

@app.route('/')
@app.route('/index')   
def index():
    #return "Index"
    user = {'username': 'Peter'}
    return render_template('index.html', title='Home', user=user)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

#############
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)


    return render_template("success_upload.html") 


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name