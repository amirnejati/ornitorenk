from flask import request, jsonify

from ornitorenk.start_srv import app
from ..controller import ServerAgent


@app.route('/srv/agents', methods=['POST'])
def server_agent_create():
    dto = request.get_json()
    r = ServerAgent().server_agents_create(**dto)
    return jsonify(r)


@app.route('/srv/agents/<agent_id>', methods=['PUT'])
def server_agent_edit(agent_id):
    dto = request.get_json()
    dto['guid'] = agent_id
    r = ServerAgent().server_agents_edit(**dto)
    return jsonify(r)


@app.route('/srv/agents/<agent_id>', methods=['DELETE'])
def server_agent_remove(agent_id):
    dto = {'agent_id': agent_id}
    r = ServerAgent().server_agents_remove(**dto)
    return jsonify(r)


@app.route('/srv/agents', methods=['GET'])
def server_agent_get():
    qs = request.query_string.decode()
    dto = qs  # fixme
    r = ServerAgent().server_agents_get_all(**dto)
    return jsonify(r)
