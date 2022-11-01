from matplotlib.pyplot import get
import pandas as pd
import numpy as np
import requests
from nba_api.stats import endpoints

def get_league_leaders_data():
    data = endpoints.leagueleaders.LeagueLeaders()

    df = data.league_leaders.get_data_frame()

    print(df.head())

def get_league_standings_data():
    data = endpoints.leaguestandings.LeagueStandings()
    
    df = data.standings.get_data_frame()

    print(df.head())

def main():
    get_league_leaders_data()
    get_league_standings_data()

if __name__ == "__main__":
    main();