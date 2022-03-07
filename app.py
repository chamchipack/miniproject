from flask import Flask, render_template


app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ikzrb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.caffe

@app.route("/caffe", methods=["GET"])
def caffe_get():
    name_receive = request.form['name_give']
    score_receive = request.form['score_give']
    add_receive = request.form['add_give']
    add_num = request.form['num_give']
    comment_num = request.form['comment_give']
#
#     # 일단 망고 플레이트- 필터 - 서울(강남) - 카페에 있는 걸 몽고 db에 직접 추가, 연결 완료, 각 개체 받는 것까지만 완료.
#     # 카페의 db 경로는 collection name = caffe / 서울은 caffe / 경기는 Gyeonggi

@app.route("/Gyeonggi", methods=["GET"])
def Gyeonggi_get():
    name_receive = request.form['name_give']
    score_receive = request.form['score_give']
    add_receive = request.form['add_give']
    add_num = request.form['num_give']
    comment_num = request.form['comment_give']

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/register')
def detail():
    return render_template("register.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
