from flask import render_template 
from flask import request, redirect, flash
from flask_wtf import FlaskForm


from werkzeug.utils import secure_filename
from app import app
from pathlib import Path
import os
from os.path import dirname

UPLOAD_FOLDER = os.path.join(dirname(dirname(os.path.realpath(__file__))), 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:
            image = request.files["image"]
            filename = secure_filename(image.filename)
            #flash("Image saved.")   # using flash requires setting o a secret key

            # TODO: replace this part with a function to upload to s3
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #return redirect(request.url)
            

    return render_template("upload.html", filename=filename) 


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name