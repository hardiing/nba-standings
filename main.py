# from matplotlib.pyplot import get
import pandas as pd
import numpy as np
import requests
from nba_api.stats import endpoints
import psycopg2
from config import config

def get_league_leaders_data():
    data = endpoints.leagueleaders.LeagueLeaders()

    df = data.league_leaders.get_data_frame()

    print(df.head())

def get_league_standings_data():
    data = endpoints.leaguestandings.LeagueStandings()
    
    df = data.standings.get_data_frame()

    print(df.head())

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
    # get_league_leaders_data()
    # get_league_standings_data()
    connect_to_psql()

if __name__ == "__main__":
    main()