import uuid
from datetime import datetime

from ornitorenk.apps.server.server_db_conn import db_conn


__author__ = "ornitorenk"


class ServerLog:

    guid = None  # PK
    service_id = None  # FK
    agent_id = None  # FK
    dt = None  # datetime
    state = None  # bool-up/down
    result = None

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex
        self.dt = datetime.now()

    def server_logs_create(self, **kwargs):
        raise NotImplementedError()

    def server_logs_edit(self, **kwargs):
        raise NotImplementedError()

    def server_logs_remove(self, **kwargs):
        raise NotImplementedError()

    def server_logs_get_all(self, **kwargs):
        raise NotImplementedError()

    def server_logs_get_last(self, **kwargs):
        # get_last: status
        raise NotImplementedError()
