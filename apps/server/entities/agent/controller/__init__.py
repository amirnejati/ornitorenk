import uuid

from ornitorenk.apps.agent.agent_db_conn import db_conn


__author__ = "ornitorenk"


class ServerAgent:

    guid = None
    alias = None
    ip = None
    port = None  # up/down
    desc = None
    enabled = None  # bool

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex

    def server_agents_create(self, **kwargs):
        raise NotImplementedError()

    def server_agents_edit(self, **kwargs):
        raise NotImplementedError()

    def server_agents_remove(self, **kwargs):
        raise NotImplementedError()

    def server_agents_get_all(self, **kwargs):
        raise NotImplementedError()
