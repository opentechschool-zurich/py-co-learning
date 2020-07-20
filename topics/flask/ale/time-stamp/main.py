from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db', 'dbTest.db')
db = SQLAlchemy(app)

class Log_entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(80), nullable=True)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return '<Timestamp %r>' % self.timestamp

@app.route('/', methods=['GET'])
def get_index():
    # TODO: read the list of log entries
    return render_template('index.html', log_entries=[])

@app.route('/', methods=['POST'])
def post_index():
    # TODO: add one log entry
    # TODO: read the list of log entries
    return render_template('index.html', log_entries=['jetzt!'])
