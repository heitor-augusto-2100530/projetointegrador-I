from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'tws_bd.mysql.dbaas.com.br'
app.config['MYSQL_USER'] = 'tws_bd'
app.config['MYSQL_PASSWORD'] = 'RecDig2@20'
app.config['MYSQL_DB'] = 'tws_bd'
mysql = MySQL(app)

@app.route("/")
def index_html():
    query = '''select * from pi_category'''
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", categorias=data)

@app.route("/category")
def category_html():
    category_id = request.args.get('id')
    category_name = request.args.get('name')
    query_skus = f'''SELECT id, name, image from pi_sku where category_id = {category_id}'''
    cur = mysql.connection.cursor()
    cur.execute(query_skus)
    data = cur.fetchall()
    cur.close()
    return render_template("category.html", skus=data, name=category_name)

@app.route("/product")
def product_html():
    sku_id = request.args.get('id')
    query_sku = f'''SELECT name, description, image from pi_sku where id = {sku_id}'''
    cur = mysql.connection.cursor()
    cur.execute(query_sku)
    data = cur.fetchone()
    cur.close()
    return render_template("product.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)