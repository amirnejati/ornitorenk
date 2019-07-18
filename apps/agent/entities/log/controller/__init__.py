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

    def agent_logs_fetch_all(self, **kwargs):
        c = self._db_conn.cursor()
        c.execute('select * from logs')
        yield c.fetchall()
        c.execute('delete from logs')
        self._db_conn.commit()

    def agent_logs_create(self, **kwargs):
        """This method calls by Celery"""
        keys = [k for k in kwargs.keys()]
        values = [[kwargs[k] for k in keys]]
        keys.append('guid')
        values[0].append(self.guid)
        c = self._db_conn.cursor()
        insert_script = 'INSERT INTO logs ({columns}) VALUES ({values});'.format(
            columns=','.join(keys),
            values=','.join('?' * len(keys)))
        c.execute(insert_script)
        c.executemany(insert_script, values)
        self._db_conn.commit()
