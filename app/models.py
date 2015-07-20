from app import db

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Student_id = db.Column(db.Integer)
    count = db.Column(db.Integer)

    def __repr__(self):
        return 'User %r' % (self.Student_id)
