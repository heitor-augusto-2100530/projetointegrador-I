from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index_html():
    return render_template("index.html")

@app.route("/product")
def product_html():
    return render_template("product.html")

@app.route("/category")
def category_html():
    return render_template("category.html")