import sqlite3

db_conn = sqlite3.connect('agent.db')


def _initiate_services():
    script = """
    CREATE TABLE IF NOT EXISTS services (
     guid TEXT PRIMARY KEY,
     service_id TEXT NOT NULL,
     dt INTEGER,
     state numeric,
     result text,

        guid text primary key,
        name text,
        script_cmd text,
        script_type text,
        timeout integer,
        retry integer,
        cron_txt text,
        enabled numeric 
    );
    """
    c = db_conn.cursor()
    c.execute(script)
    db_conn.commit()


def _initiate_logs():
    script = """
    CREATE TABLE IF NOT EXISTS logs (
     guid TEXT PRIMARY KEY,
     service_id TEXT NOT NULL,
     dt INTEGER,
     state numeric,
     result text,
     
     CONSTRAINT FK_Service
     FOREIGN KEY (service_id)
     REFERENCES services(guid) 
    );
    """
    c = db_conn.cursor()
    c.execute(script)
    db_conn.commit()

