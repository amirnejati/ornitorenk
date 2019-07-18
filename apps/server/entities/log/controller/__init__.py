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
