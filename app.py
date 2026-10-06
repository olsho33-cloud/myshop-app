from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>myshop.com 메인 페이지</h1><p>서비스가 정상 가동 중입니다.</p>"

@app.route('/api/cart')
def cart():
    return jsonify({
        "status": "success",
        "cart_items": [
            {"id": 1, "name": "무선 키보드", "price": 45000},
            {"id": 2, "name": "게이밍 마우스", "price": 32000}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
