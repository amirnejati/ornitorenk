from flask import request, jsonify

from ornitorenk.start_agt import app
from ..controller import AgentLog


@app.route('/agt/logs', methods=['GET'])
def agent_logs_fetch_all():
    qs = request.query_string.decode()
    dto = qs  # fixme
    r = AgentLog().agent_logs_fetch_all(**dto)
    return jsonify(r)
