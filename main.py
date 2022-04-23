from flask import Flask, render_template
from __init__ import app


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