import uuid

from ornitorenk.apps.agent.db_connection import db_conn


__author__ = "ornitorenk"


class AgentLog:

    guid = None
    service_id = None  # FK
    dt = None
    state = None  # up/down
    result = None

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex
