import uuid

from ornitorenk.apps.server.server_db_conn import db_conn


__author__ = "ornitorenk"


class ServerService:

    guid = None  # PK
    name = None
    script_cmd = None
    script_type = None  # bash/python
    timeout = None  # up/down
    retry = None
    cron_txt = None
    enabled = None  # bool
    agent_id = None  # FK

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex

    def server_services_create(self, **kwargs):
        raise NotImplementedError()

    def server_services_edit(self, **kwargs):
        raise NotImplementedError()

    def server_services_remove(self, **kwargs):
        raise NotImplementedError()

    def server_services_get_all(self, **kwargs):
        raise NotImplementedError()
