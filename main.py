# from matplotlib.pyplot import get
import pandas as pd
import numpy as np
import requests
from nba_api.stats import endpoints
import psycopg2
from config import config
from create_tables import create_tables

def connect_to_psql():
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to PostgreSQL server
        print("Connecting to PostgreSQL...")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print("PostgreSQL database version:")
        cur.execute("SELECT version();")

        # display PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close connection to PostgreSQL
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")

def main():
    connect_to_psql()
    create_tables()

if __name__ == "__main__":
    main()