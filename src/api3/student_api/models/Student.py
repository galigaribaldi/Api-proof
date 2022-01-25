from api3 import db
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
    def __repr__(self):
        return 'Task Id: %d, NAme: %s, Duracion: %d' % (self.id, self.name, self.age)