from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import psycopg2
import os


def connect():
    con = psycopg2.connect(dbname='geodatabase',
                        user='postgres', host='localhost',
                        password='1234')

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
    con.set_session(autocommit=True)
    cur = con.cursor()
    # cur.execute(sql.SQL("SELECT pg_terminate_backend(pg_stat_activity.pid)\
    #                     FROM pg_stat_activity\
    #                     WHERE datname='geodatabase'\
    #                     AND pid <> pg_backend_pid()\
    #                     "))
    # cur.execute(sql.SQL("drop database geodatabase"))
    cur.execute(
        """SELECT 'CREATE DATABASE geodatabase_hackathon' WHERE NOT EXISTS(SELECT FROM pg_database WHERE datname= 'geotabase')""")
    cur.execute("""create extension IF NOT EXISTS postgis""")
    cur.execute("""DROP TABLE IF EXISTS trajectories""")
    cur.execute("""CREATE TABLE trajectories(
        index int NOT NULL PRIMARY KEY,
        id int NOT NULL,
        day int NOT NULL,
        longitude float NOT NULL,
        latitude float NOT NULL)
        """)
    
    return con, cur

def close_connection(con, cur):
    cur.close()
    con.close()

def insert_data(cur, folder):
    for file in os.listdir(folder):
        print(os.path.join(folder, file))
        if os.path.isfile(os.path.join(folder, file)):
            with open(os.path.join(folder, file), 'r') as f:
                # Notice that we don't need the `csv` module.
                next(f)  # Skip the header row.
                cur.copy_from(f, 'trajectories', sep=',')

if __name__ == "__main__":
    con, cur = connect()
    insert_data(cur, "../datasets");
    close_connection(con, cur);
    
