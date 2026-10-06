from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>myshop.com 메인 페이지</h1><p>서비스가 정상 가동 중입니다.</p>"

@app.route('/api/cart')
def cart():
    # 의도적 버그 주입: 존재하지 않는 변수 참조로 인한 500 에러 발생
    raise Exception("Critical Database Connection Failed! (의도적 장애 발생)")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
