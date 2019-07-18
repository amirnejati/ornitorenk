from flask import request, jsonify

from ornitorenk.start_agt import agt_bp
from ..controller import AgentLog


@agt_bp.route('/logs', methods=['GET'])
def agent_logs_fetch_all():
    qs = request.query_string.decode()
    dto = qs  # fixme
    # r = AgentLog().agent_logs_fetch_all(**dto)
    r = {'x': 'y'}
    return jsonify(r)
