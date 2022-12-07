from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import pandas as pd
from nba_api.stats import endpoints
from config import config
from create_tables import create_tables

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

if __name__ == "__main__":
    main()