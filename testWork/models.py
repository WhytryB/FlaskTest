from app import database as db


class DateTimeEvent(db.Model):
    __tablename__ = 'Event'

    Date = db.Column(db.DateTime, primary_key=True)

    def __init__(self, Date):
        self.Date = Date

    def __repr__(self):
        return '<Date {}>'.format(self.Date)
