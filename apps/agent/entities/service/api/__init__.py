from flask import request, jsonify

from ornitorenk.start_agt import app
from ..controller import AgentService


@app.route('/agt/services', methods=['POST'])
def agent_service_create():
    dto = request.get_json()
    r = AgentService().agent_services_create(**dto)
    return jsonify(r)


@app.route('/agt/services/<service_id>', methods=['PUT'])
def agent_service_edit(service_id):
    dto = request.get_json()
    dto['guid'] = service_id
    r = AgentService().agent_services_edit(**dto)
    return jsonify(r)


@app.route('/agt/services/<service_id>', methods=['DELETE'])
def agent_service_remove(service_id):
    dto = {'service_id': service_id}
    r = AgentService().agent_services_remove(**dto)
    return jsonify(r)


# @app.route('/agt/services', methods=['GET'])
# def agent_service_get():
#     qs = request.query_string.decode()
#     raise NotImplementedError()
