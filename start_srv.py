from flask import Flask, Blueprint

app = Flask(__name__)
srv_bp = Blueprint("server", __name__, template_folder='templates')


def start_server():
    from ornitorenk.apps.server.entities.log.api import srv_bp
    from ornitorenk.apps.server.entities.service.api import srv_bp
    from ornitorenk.apps.server.entities.agent.api import srv_bp

    app.register_blueprint(srv_bp, url_prefix='/srv')
    app.run(host='127.0.0.1', port=8080, threaded=True)


if __name__ == '__main__':
    start_server()
