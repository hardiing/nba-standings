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

@app.route("/league_leaders", methods=["GET", "POST"])
def league_leaders():

    engine = create_engine(cred.string)
    conn = engine.connect()

    data = endpoints.leagueleaders.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    df.to_sql("stats", con=conn, if_exists="replace", index=False)

    cur = mysql.connection.cursor()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM stats")
    data = cursor.fetchall()
    cursor.close()
    
    return render_template("league_leaders.html")

if __name__ == "__main__":
    main()