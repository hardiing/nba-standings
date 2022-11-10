#!/usr/bin/python

import psycopg2
from config import config
from nba_api.stats import endpoints
from sqlalchemy import create_engine
import cred

def get_league_leaders_data():
    engine = create_engine(cred.string)
    conn = engine.connect()

    data = endpoints.leagueleaders.LeagueLeaders()

    df = data.league_leaders.get_data_frame()
    df.to_sql("stats", con=conn, if_exists="replace", index=False)
    conn = psycopg2.connect(host="localhost", user=cred.user, password=cred.password, dbname="nba-standings")
    conn.autocommit = True
    conn.commit()
    conn.close()

def get_league_standings_data():
    engine = create_engine(cred.string)
    conn = engine.connect()

    data = endpoints.leaguestandings.LeagueStandings()
    
    df = data.standings.get_data_frame()
    df.to_sql("standings", con=conn, if_exists="replace", index=False)
    conn = psycopg2.connect(host="localhost", user=cred.user, password=cred.password, dbname="nba-standings")
    conn.autocommit = True
    conn.commit()
    conn.close()

def create_tables():
    get_league_leaders_data()
    get_league_standings_data()