from datetime import datetime

import os
from flask import Flask, redirect, request, render_template, url_for, send_file, send_from_directory, safe_join, abort
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('about.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/artwork')
def artwork():
    return render_template('artwork.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/email')
def email():
    return render_template('email.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


# --------------- Blog posts ---------------


@app.route('/post/subdivision')
def subdivision():
    return render_template('/blogposts/subdivision.html')


@app.route('/post/lighting')
def lighting():
    return render_template('/blogposts/lighting.html')


@app.route('/post/big-o')
def bigO():
    return render_template('/blogposts/big-o.html')


@app.route('/post/sorting')
def sorting():
    return render_template('/blogposts/sorting.html')


# -------------- Projects -------------------


@app.route('/attraction')
def attraction():
    return render_template('/projects/attractor.html')

# ----------------- API ---------------------


@app.route('/api/btc', methods=['GET'])
def backingTrackCreator():
    if request.method == "GET":
        try:

            url = 'http://73.8.81.211:8000/api/btc?url='
            url += request.args.get('url')

            return redirect(url)

        except Exception as e:
            return str(e)
    else:
        return '500'


if __name__ == '__main__':
    app.run(debug=True)
