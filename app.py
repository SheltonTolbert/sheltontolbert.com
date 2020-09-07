from datetime import datetime

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


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


@app.route('/post1')
def post1():
    return render_template('/blogposts/template.html')


if __name__ == '__main__':
    app.run(debug=True)
