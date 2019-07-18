import uuid

from ornitorenk.apps.agent.db_connection import db_conn


__author__ = "ornitorenk"


class AgentService:

    guid = None
    name = None
    bash_txt = None
    timeout = None  # up/down
    retry = None
    cron_txt = None
    enabled = None  # bool

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex
