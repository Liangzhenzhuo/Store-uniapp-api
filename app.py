from flask import Flask, make_response, jsonify
from flask_cors import *

app = Flask(__name__)
# 跨域
CORS(app, supports_credentials=True)


@app.route('/getSwiper', methods=["POST"])
def getSwiper():
    data = [
        {
            'title': 'Nike React Vision',
            'content': '男子运动鞋演绎非凡舒适体验',
            'id': 1,
            'style': 'oringe',
            'pic': '/static/images/goods/Nike React Vision/Nike React Vision 1.jpg'
        },
        {
            'title': 'Nike NSW React Vision',
            'content': '灵感来源于墨西哥民间艺术神话人物',
            'id': 2,
            'style': 'blue',
            'pic': '/static/images/goods/Nike NSW React Vision/Nike NSW React Vision 1.jpg'
        },
        {
            'title': 'Jumpman Diamond Low PF',
            'content': '汀克·哈特菲尔德亲自设计',
            'id': 3,
            'style': 'red',
            'pic': '/static/images/goods/Jumpman Diamond Low PF/Jumpman Diamond Low PF 1.jpg'
        }
    ]
    response = make_response(jsonify(data))
    return response


@app.route('/getPopular', methods=["POST"])
def getPopular():
    data = [
        {
            'pic': '/static/images/most-popular/1.png'
        },
        {
            'pic': '/static/images/most-popular/2.png'
        },
        {
            'pic': '/static/images/most-popular/3.png'
        },
        {
            'pic': '/static/images/most-popular/4.png'
        },
        {
            'pic': '/static/images/most-popular/5.png'
        },
        {
            'pic': '/static/images/most-popular/5.png'
        }
    ]
    response = make_response(jsonify(data))
    return response


@app.route('/getDiscover', methods=["POST"])
def getDiscover():
    data = [
        {
            'pic': '/static/images/discover/1.jpg'
        },
        {
            'pic': '/static/images/discover/2.jpg'
        },
        {
            'pic': '/static/images/discover/3.jpg'
        },
        {
            'pic': '/static/images/discover/4.jpg'
        },
        {
            'pic': '/static/images/discover/5.jpg'
        },
        {
            'pic': '/static/images/discover/6.jpg'
        }
    ]
    response = make_response(jsonify(data))
    return response


@app.route('/getCategories', methods=["POST"])
def getCategories():
    data = [
        {
            'title': '数码3C',
            'pic': '/static/images/category/mobiles.png'
        },
        {
            'title': '全球购',
            'pic': '/static/images/category/earth.png'
        },
        {
            'title': '时尚',
            'pic': '/static/images/category/fashion.png'
        },
        {
            'title': '家电',
            'pic': '/static/images/category/jiadian.png'
        }
    ]
    response = make_response(jsonify(data))
    return response


@app.route('/getGoods', methods=["POST"])
def getGoods():
    data = [
        {
            'title': 'Jumpman Diamond Low PF',
            'pic': '/static/images/goods/Jumpman Diamond Low PF/Jumpman Diamond Low PF 1.jpg',
            'price': 300,
            'originPrice': 720
        },
        {
            'title': 'Nike NSW React Vision',
            'pic': '/static/images/goods/Nike NSW React Vision/Nike NSW React Vision 1.jpg',
            'price': 200,
            'originPrice': 650
        },
        {
            'title': 'Nike React Vision',
            'pic': '/static/images/goods/Nike React Vision/Nike React Vision 1.jpg',
            'price': 700,
            'originPrice': 1300
        }
    ]
    response = make_response(jsonify(data))
    return response


if __name__ == '__main__':
    app.run()
