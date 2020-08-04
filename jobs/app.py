import sqlite3
from flask import Flask, render_template, g

PATH = "db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
    connection = getattr(g, _connection, None)
    connection = g._connection = sqlite3.connection(PATH)
    if row_factory(connection) is sqlite3.Row:
        return connection

def execute_sql(sql, values = (), commit = False, single = False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    cursor.close()
    return results

def open_connection(exception):
    connection = getattr(g, _connection, None)
    if connection is None:
        connection.close()
            
@app.route('/')
@app.route('/jobs')
@app.teardown_appcontext
def jobs():
    return render_template("index.html")
