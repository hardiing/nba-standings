from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import pandas as pd
from nba_api.stats import endpoints
from sqlalchemy import create_engine
import cred

#  connect flask and MySQL
app = Flask(__name__)
app.config["MYSQL_HOST"] = "db"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_DB"] = "nba"

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
#  return index page to start
def main():
    return render_template("index.html")

@app.route("/ppg", methods=["GET", "POST"])
def ppg():

    # create sqlalchemy engine to connect to database
    engine = create_engine(cred.string)
    conn = engine.connect()

    # get data from API endpoint, create a dataframe from it, and convert it to an SQL table
    data = endpoints.leagueleaders.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    df.to_sql("stats", con=conn, if_exists="replace", index=False)

    # define headings for HTML table
    headings = ("Player", "Team", "GP", "PPG", "RPG", "APG", "SPG", "BPG")
    
    # connect to MySQL table, execute query, fetch the data, and close the connection
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT PLAYER, TEAM, GP, (PTS/GP) AS PPG, (REB/GP) AS RPG, (AST/GP) AS APG, (STL/GP) AS SPG, (BLK/GP) AS BPG FROM stats ORDER BY PPG DESC LIMIT 10;")
    data = cursor.fetchall()
    cursor.close()
    
    # return page with table made with headings and data
    return render_template("ppg.html", headings=headings, data=data)

@app.route("/rpg", methods=["GET", "POST"])
def rpg():

    # create sqlalchemy engine to connect to database
    engine = create_engine(cred.string)
    conn = engine.connect()

    # get data from API endpoint, create a dataframe from it, and convert it to an SQL table
    data = endpoints.leagueleaders.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    df.to_sql("stats", con=conn, if_exists="replace", index=False)

    # define headings for HTML table
    headings = ("Player", "Team", "GP", "PPG", "RPG", "APG", "SPG", "BPG")

    # connect to MySQL table, execute query, fetch the data, and close the connection
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT PLAYER, TEAM, GP, (PTS/GP) AS PPG, (REB/GP) AS RPG, (AST/GP) AS APG, (STL/GP) AS SPG, (BLK/GP) AS BPG FROM stats ORDER BY RPG DESC LIMIT 10;")
    data = cursor.fetchall()
    cursor.close()

    # return page with table made with headings and data
    return render_template("rpg.html", headings=headings, data=data)

@app.route("/apg", methods=["GET", "POST"])
def apg():

    # create sqlalchemy engine to connect to database
    engine = create_engine(cred.string)
    conn = engine.connect()

    # get data from API endpoint, create a dataframe from it, and convert it to an SQL table
    data = endpoints.leagueleaders.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    df.to_sql("stats", con=conn, if_exists="replace", index=False)

    # define headings for HTML table
    headings = ("Player", "Team", "GP", "PPG", "RPG", "APG", "SPG", "BPG")

    # connect to MySQL table, execute query, fetch the data, and close the connection
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT PLAYER, TEAM, GP, (PTS/GP) AS PPG, (REB/GP) AS RPG, (AST/GP) AS APG, (STL/GP) AS SPG, (BLK/GP) AS BPG FROM stats ORDER BY APG DESC LIMIT 10;")
    data = cursor.fetchall()
    cursor.close()

    # return page with table made with headings and data
    return render_template("apg.html", headings=headings, data=data)

@app.route("/league_standings", methods=["GET", "POST"])
def league_standings():

    # create sqlalchemy engine to connect to database
    engine = create_engine(cred.string)
    conn = engine.connect()

    # get data from API endpoint, create a dataframe from it, and convert it to an SQL table
    data = endpoints.leaguestandings.LeagueStandings()
    df = data.standings.get_data_frame()
    df.to_sql("standings", con=conn, if_exists="replace", index=False)

    # define headings for HTML table
    headings = ("Rank", "Team", "Record", "Home Record", "Road Record", "L10", "PPG", "Opp PPG", "Opp Over .500", "Post ASB")

    # connect to MySQL table, execute query, fetch the data, and close the connection
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT PlayoffRank, TeamCity, Record, HOME, ROAD, L10, PointsPG, OppPointsPG, OppOver500, PostAS FROM standings ORDER BY PlayoffRank;")
    data = cursor.fetchall()
    cursor.close()

    # return page with table made with headings and data
    return render_template("league_standings.html", headings=headings, data=data)

if __name__ == "__main__":
    main()