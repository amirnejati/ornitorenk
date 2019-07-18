import uuid
from datetime import datetime

from ornitorenk.apps.agent.agent_db_conn import db_conn


__author__ = "ornitorenk"


class AgentLog:

    guid = None  # PK
    service_id = None  # FK
    dt = None  # datetime
    state = None  # bool-up/down
    result = None

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex
        self.dt = datetime.now()
