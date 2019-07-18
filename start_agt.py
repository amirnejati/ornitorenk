from flask import Flask

app = Flask(__name__)


def start_agent():
    app.run(host='127.0.0.1', port=8080, threaded=True)


if __name__ == '__main__':
    start_agent()
