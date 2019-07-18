import subprocess
import time

from ornitorenk.apps.agent.agent_db_conn import db_conn
from ornitorenk.apps.agent.entities.log.controller import AgentLog


def cronize_function(duration, cycle, fn, *args):
    while duration > 0:
        yield fn(*args)
        duration -= cycle
        if duration < cycle:
            break
        time.sleep(cycle)


def task(cmd):
    return subprocess.Popen([cmd])


c =db_conn.cursor()
c.execute('select * from services')
for s in c.fetchall():
    service_id = s[0]
    script_cmd = s[2]
    r = cronize_function(5 * 60 * 60, 5, task, script_cmd)
    AgentLog().agent_logs_create(service_id=service_id, state=r)
