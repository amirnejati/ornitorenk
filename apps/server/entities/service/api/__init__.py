from flask import request, jsonify

from ornitorenk.start_srv import app
from ..controller import ServerService


@app.route('/srv/services', methods=['POST'])
def server_service_create():
    dto = request.get_json()
    r = ServerService().server_services_create(**dto)
    return jsonify(r)


@app.route('/srv/services/<service_id>', methods=['PUT'])
def server_service_edit(service_id):
    dto = request.get_json()
    dto['guid'] = service_id
    r = ServerService().server_services_edit(**dto)
    return jsonify(r)


@app.route('/srv/services/<service_id>', methods=['DELETE'])
def server_service_remove(service_id):
    dto = {'service_id': service_id}
    r = ServerService().server_services_remove(**dto)
    return jsonify(r)


@app.route('/srv/services', methods=['GET'])
def server_service_get():
    qs = request.query_string.decode()
    dto = qs  # fixme
    r = ServerService().server_services_get_all(**dto)
    return jsonify(r)
