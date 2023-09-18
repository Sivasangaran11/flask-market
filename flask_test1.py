from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import csv
app=Flask(__name__)#__name__ evaluates the name of the current module 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db=SQLAlchemy(app)
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=38), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1824), nullable=False, unique=True)
@app.route('/')
def hello_world():
    return render_template('base.html')
@app.route("/home")
def home():
    return render_template('home.html')
@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html',item=items)
"""def market():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}]
    with open("market.csv","w",newline="")as market:
        csvwriter=csv.writer(market)
        csvwriter.writerow(["ID","NAME","BARCODE","PRICE"])
        for item in items:
            csvwriter.writerow([item.get('id'),item.get('name'),item.get('barcode'),item.get('price')])
    market.close()
market()"""
