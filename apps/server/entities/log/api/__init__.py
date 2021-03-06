from flask import request, jsonify

from ornitorenk.start_srv import srv_bp
from ..controller import ServerLog


@srv_bp.route('/logs', methods=['POST'])
def agent_logs_create():
    dto = request.get_json()
    r = ServerLog().server_logs_create(**dto)
    return jsonify(r)


@srv_bp.route('/logs/<log_id>', methods=['PUT'])
def agent_logs_edit(log_id):
    dto = request.get_json()
    dto['guid'] = log_id
    r = ServerLog().server_logs_edit(**dto)
    return jsonify(r)


@srv_bp.route('/logs/<log_id>', methods=['DELETE'])
def agent_logs_remove(log_id):
    dto = {'service_id': log_id}
    r = ServerLog().server_logs_remove(**dto)
    return jsonify(r)


@srv_bp.route('/logs', methods=['GET'])
def agent_logs_get():
    qs = request.query_string.decode()
    r = ServerLog().server_logs_get_all()
    return jsonify(r)


@srv_bp.route('/status', methods=['GET'])
def agent_logs_status():
    qs = request.query_string.decode()
    r = ServerLog().server_logs_get_last()
    return jsonify(r)
