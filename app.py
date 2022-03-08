from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
import certifi
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ikzrb.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
    #
    caffe_list = list(db.caffe.find({}, {'_id': False}))
    #
    return render_template('index.html', caffe_list=caffe_list)

@app.route("/caffe", methods=["GET"])
def caffe_get():
    caffe_list = list(db.caffe.find({}, {'_id': False}))
    print(caffe_list)
    return jsonify({'Seoul':caffe_list})


@app.route("/Gyeonggi", methods=["GET"])
def Gyeonggi_get():
    Gyeonggi_list = list(db.Gyeonggi.find({}, {'_id': False}))
    return jsonify({'Gyeonggii':Gyeonggi_list})

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/register')
def detail():
    return render_template("register.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
