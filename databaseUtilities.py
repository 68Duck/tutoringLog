import sqlite3
from flask import g,Flask,render_template,request



DATABASE = 'tutorLog.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def getTableNames():
    return query_db("SELECT name FROM sqlite_master WHERE type='table';")

def checkIfTableExisits(tableName):  #returns true or false if exisits or not
    results = query_db('SELECT name FROM sqlite_master WHERE type="table" AND name="{0}";'.format(tableName))
    if len(results)==1:
        return True
    else:
        return False
