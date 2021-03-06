from flask import Flask, make_response, jsonify, request
from flask_cors import *
from DbHandle import *

app = Flask(__name__)
# 跨域
CORS(app, supports_credentials=True)
DbHandle = DataBaseHandle('47.240.161.245','StoreUniappApi','SDKa5jpJFERiPJY6','StoreUniappApi', 3306)


@app.route('/getSwiper', methods=["POST"])
def getSwiper():
    res = DbHandle.selectDb('select * from swiper')
    data = []
    if res:
        for i in res:
            data.append(
                {
                    'id': i[0],
                    'title': i[1],
                    'content': i[2],
                    'style': i[3],
                    'pic': i[4]
                }
            )
    response = make_response(jsonify(data))
    return response


@app.route('/getPopular', methods=["POST"])
def getPopular():
    res = DbHandle.selectDb('select * from popular')
    data = []
    if res:
        for i in res:
            data.append(
                {
                    'pic': i[1]
                }
            )
    response = make_response(jsonify(data))
    return response


@app.route('/getDiscover', methods=["POST"])
def getDiscover():
    res = DbHandle.selectDb('select * from discover')
    data = []
    if res:
        for i in res:
            data.append(
                {
                    'pic': i[1]
                }
            )
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
    res = DbHandle.selectDb('select * from goods')
    data = []
    if res:
        for i in res:
            res2 = DbHandle.selectDb('select pic_address from good_images where good_id="{}"'.format(i[0]))
            pics = [x[0] for x in res2]
            data.append(
                {
                    'id': i[0],
                    'title': i[1],
                    'price': float(i[2]),
                    'originPrice': float(i[3]),
                    'pic': pics
                }
            )
    response = make_response(jsonify(data))
    return response


@app.route('/getGoodInfoById', methods=["POST"])
def getGoodInfoById():
    id = request.form.get('id')
    res = DbHandle.selectDb('select * from goods where id="{}"'.format(id))
    data = []
    if res:
        for i in res:
            res2 = DbHandle.selectDb('select pic_address from good_images where good_id="{}"'.format(i[0]))
            pics = [x[0] for x in res2]
            data.append(
                {
                    'id': i[0],
                    'title': i[1],
                    'price': float(i[2]),
                    'originPrice': float(i[3]),
                    'pic': pics
                }
            )
    response = make_response(jsonify(data))
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
