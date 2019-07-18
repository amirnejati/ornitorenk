from flask import Flask, Blueprint

app = Flask(__name__)
agt_bp = Blueprint("agent", __name__, template_folder='templates')


def start_agent():
    from ornitorenk.apps.agent.entities.log.api import  agt_bp
    from ornitorenk.apps.agent.entities.service.api import agt_bp

    app.register_blueprint(agt_bp, url_prefix='/agt')
    app.run(host='127.0.0.1', port=8081, threaded=True)


if __name__ == '__main__':
    start_agent()
