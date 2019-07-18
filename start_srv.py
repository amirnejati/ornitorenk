from flask import Flask

app = Flask(__name__)


def start_server():
    app.run(host='127.0.0.1', port=8081, threaded=True)


if __name__ == '__main__':
    start_server()
