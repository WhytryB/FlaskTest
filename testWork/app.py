from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template
import datetime
import os


app = Flask(__name__)
app.config.from_object("config.Config")
database = SQLAlchemy(app)
migrate = Migrate(app, database)

from models import DateTimeEvent


@app.route('/')
def hello():
    print(datetime.datetime.utcnow)
    data_event_object = DateTimeEvent(Date=datetime.datetime.now())
    database.session.add(data_event_object)
    database.session.commit()

    event_objects = DateTimeEvent.query.all()

    return render_template('DataFrame.html', EventObjects=event_objects)


if __name__ == '__main__':
    app.run()