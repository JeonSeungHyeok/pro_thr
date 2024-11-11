from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '정보보호 9회차 전승혁<br>'+'Hello, world!<br>'*3

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    