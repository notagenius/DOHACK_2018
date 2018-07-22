from flask import Flask, render_template, json, request, g
import sqlite3

SQL_SCHEMA = '''
drop table if exists tickets;
create table tickets (
  id integer primary key autoincrement,
  title text not null,
  state text not null,
  created_at text not null,
  last_updated text not null,
  created_by text not null,
  tags text not null,
  real_time_state text not null,
  users_looking text not null,
  total_users_looking int not null,
  users_editing text not null,
  total_users_editing int not null
);
drop table if exists interactions;
create table interactions (
  id integer primary key autoincrement,
  ticket_id integer not null,
  sender text not null,
  receiver text not null,
  date text not null,
  content text not null,
  type text not null
);
drop table if exists agents;
create table agents (
  id integer primary key autoincrement,
  is_admin integer not null,
  name text not null,
  email text not null,
  password text not null
);
'''

app = Flask(__name__)

def connect_db():
    rv = sqlite3.connect('the.db')
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    db.cursor().executescript(SQL_SCHEMA)
    db.commit()

def add_mock_data():
    db = get_db()
    list_mock, interaction_mock = gen_mock_data(100)
    for l_mock in list_mock:
        cur = db.execute('insert into tickets (title, state, created_at, last_updated, created_by, tags, real_time_state, users_looking, total_users_looking, users_editing, total_users_editing) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', l_mock)
    for i_mock in interaction_mock:
        db.execute('insert into interactions (ticket_id, sender, receiver, date, content, type) VALUES (?, ?, ?, ?, ?, ?)', i_mock)    
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    #add_mock_data()
    #add_standard_agents()
    print('Initialized the database.')


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()




@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showOverview')
def showOverview():
    return render_template('overview.html')

@app.route('/showData')
def showData():
    return render_template('data.html')

@app.route('/showCounting')
def showCount():
    return render_template('counting.html')

@app.route('/showSingleMode')
def showSingleMode():
    return render_template('singlemode.html')

@app.route('/showTrackingMode')
def showTrackingMode():
    return render_template('trackingmode.html')

if __name__ == "__main__":
    app.run()
