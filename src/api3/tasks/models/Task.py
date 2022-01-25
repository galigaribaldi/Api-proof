from api3 import db

class Task(db.Model):
    
    __tablename__='task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    duration = db.Column(db.Integer)
    time_registred = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    
    def __init__(self, description, duration,time_registred, status, id):
        self.id = id
        self.description = description
        self.duration = duration
        self.time_registred = time_registred
        self.status = status
        
    def __repr__(self):
        return 'Task Id: %d, Descripcion: %s, Duracion: %d' % (self.id, self.description, self.duration)