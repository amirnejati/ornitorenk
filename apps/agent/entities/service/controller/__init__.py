import uuid

from ornitorenk.apps.agent.agent_db_conn import db_conn


__author__ = "ornitorenk"


class AgentService:

    guid = None  # PK
    name = None
    script_cmd = None
    script_type = None  # bash/python
    timeout = None  # up/down
    retry = None
    cron_txt = None
    enabled = None  # bool

    def __init__(self):
        self._db_conn = db_conn
        self.guid = uuid.uuid4().hex

    def agent_services_create(self, **kwargs):
        keys = [k for k in kwargs.keys()]
        values = [[kwargs[k] for k in keys]]
        keys.append('guid')
        values[0].append(self.guid)

        c = self._db_conn.cursor()
        insert_script = 'INSERT INTO services ({columns}) VALUES ({values});'.format(
            columns=','.join(keys),
            values=','.join('?' * len(keys)))
        c.execute(insert_script)
        c.executemany(insert_script, values)
        self._db_conn.commit()

    def agent_services_edit(self, **kwargs):
        raise NotImplementedError()

    def agent_services_remove(self, **kwargs):
        raise NotImplementedError()

    def agent_services_get(self, **kwargs):
        c = self._db_conn.cursor()
        c.execute('select * from services')
        return c.fetchall()
