from flask import render_template
from __init__ import app
# this is where all the html pages are connected with their url locations on the website
# this allows linking pages within the code and outside of the code on the website


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/blackpink/')
def bpquiz():
    return render_template("bpquiz.html")


@app.route('/goddesses/')
def ggquiz():
    return render_template("ggquiz.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
